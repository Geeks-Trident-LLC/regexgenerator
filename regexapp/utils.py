"""
regexapp.utils
==============

Utility functions and helpers for the regexapp framework.

This module provides reusable functions to support regular expression
construction, validation, and file handling. It centralizes common logic
to reduce duplication across regexapp modules and ensures consistent
error handling, formatting, and integration with YAML configuration
files.
"""


import re
import sys
from typing import Optional
from io import IOBase

from argparse import ArgumentParser

import yaml
from genericlib import DotObject
from genericlib.constant import ECODE


class MiscArgs:
    @classmethod
    def get_parsed_result_as_data_or_file(cls, *kwflags, data: str=''):
        """
        Parse input into either inline data or a file reference.

        This method uses `argparse` to interpret the first line of the
        provided `data` string. It distinguishes between file references
        (via flags such as `--file`, `--filename`, or `--file-name`) and
        inline data values. Additional custom flags can be passed through
        `kwflags`. The result is returned as a `DotObject` with attributes
        describing the parsing outcome.

        Parameters
        ----------
        *kwflags : list of flags
            Additional flag names to accept (e.g., `--config`, `--path`).
        data : str, default is empty string
            Input string to parse. Only the first line is inspected for
            flags. Defaults to an empty string.

        Returns
        -------
        DotObject
            A structured result with the following attributes:
            - `is_parsed` : bool
                Whether parsing succeeded.
            - `is_data` : bool
                True if the input was recognized as inline data.
            - `data` : str
                The parsed data content (if any).
            - `is_file` : bool
                True if the input was recognized as a file reference.
            - `filename` : str
                The parsed filename (if any).
            - `failure` : str
                Error message if parsing failed.

        Raises
        ------
        Exception
            Any exception raised during parsing is caught and stored in
            `failure`. The method itself does not propagate exceptions.

        Notes
        -----
        - File flags are matched case‑insensitively against the pattern
          `file`, `filename`, or `file-name`.
        - If neither data nor file input is found, `failure` is set to
          `"Invalid data"`.
        - The method inspects only the first line of `data` for flags.
        """
        parser = ArgumentParser(exit_on_error=False)
        parser.add_argument('val1', nargs='*')
        parser.add_argument('--file', type=str, default='')
        parser.add_argument('--filename', type=str, default='')
        parser.add_argument('--file-name', type=str, default='')
        for flag in kwflags:
            parser.add_argument(flag, type=str, default='')
        parser.add_argument('val2', nargs='*')

        data = str(data).strip()
        first_line = '\n'.join(data.splitlines()[:1])
        pattern = '(?i)file(_?name)?$'

        result = DotObject(
            is_parsed=False, is_data=False, data=data,
            is_file=False, filename='', failure=''
        )

        try:
            options = parser.parse_args(re.split(r' +', first_line))
            result.is_parsed = True
            for flag, val in vars(options).items():
                if re.match(pattern, flag) and val.strip():
                    result.is_file = True
                    result.filename = val.strip()
                else:
                    if flag != 'val1' or flag != 'val2':
                        if val.strip():
                            result.is_data = True
                            result.data = val.strip()
                            return result

            if result.val1 or result.val2:
                result.is_data = True
                return result
            else:
                result.is_parsed = False
                result.failure = 'Invalid data'
                return result

        except Exception as ex:
            result.failure = f'{type(ex).__name__}: {ex}'
            result.is_parsed = False
            return result


class File:
    """
    Utility class for file operations within the regexapp framework.

    Provides safe and consistent methods for reading, writing, and
    parsing files, with a focus on YAML configuration files used by
    regexapp. This class centralizes file handling logic to ensure
    maintainability, error handling, and consistent encoding practices.

    Raises
    ------
    OSError
        If a file cannot be opened or read.
    ValueError
        If a filename or file content is empty when required.
    yaml.YAMLError
        If YAML content is invalid or cannot be parsed.
    """
    @classmethod
    def get_file_stream(
        cls,
        filename: str,
        mode: str = "r",
        buffering: int = -1,
        encoding: Optional[str] = None,
        errors: Optional[str] = None,
        newline: Optional[str] = None,
        closefd: bool = True,
        opener=None
    ) -> IOBase:
        """
        Open a file and return its stream.

        Parameters
        ----------
        filename : str
            Path to the file to open.
        mode : str, default 'r'
            File mode (e.g., 'r', 'w', 'a', 'rb').
        buffering : int, default -1
            Buffering policy (-1 uses system default).
        encoding : str, optional
            Encoding to use for text mode.
        errors : str, optional
            Error handling scheme for encoding/decoding.
        newline : str, optional
            Controls universal newlines mode.
        closefd : bool, default True
            If False, the underlying file descriptor is kept open.
        opener : callable, optional
            Custom opener; must return an open file descriptor.

        Returns
        -------
        IOBase
            An open file stream ready for reading or writing.

        Raises
        ------
        ValueError
            If `filename` is empty after normalization.
        OSError
            If the file cannot be opened.
        """
        filename = str(filename)
        if not filename:
            raise ValueError("Filename cannot be empty.")

        try:
            kwargs = dict(
                mode=mode, buffering=buffering, encoding=encoding,
                errors=errors, newline=newline, closefd=closefd, opener=opener
            )
            stream = open(filename, **kwargs)
            return stream
        except OSError as ex:
            raise OSError(f"Failed to open file {filename}: {ex}") from ex

    @classmethod
    def read(cls, filename: str, encoding: str="utf-8"):
        """
        Read and return the full content of a file.

        This method opens the specified file using `get_file_stream` in
        read mode, reads its entire content into memory, and returns it
        as a string. By default, the file is read with UTF‑8 encoding.

        Parameters
        ----------
        filename : str
            Path to the file to read.
        encoding : str, default "utf-8"
            Text encoding used to decode the file content.

        Returns
        -------
        str
            The complete contents of the file as a string.

        Raises
        ------
        ValueError
            If `filename` is empty after normalization.
        OSError
            If the file cannot be opened or read.

        Notes
        -----
        - This method reads the entire file into memory at once. For
          very large files, consider using a streaming approach instead.
        - Relies on `get_file_stream` for consistent error handling and
          filename normalization.
        """
        stream = cls.get_file_stream(filename, mode="r", encoding=encoding)
        content = stream.read()
        return content

    @classmethod
    def read_with_exit(cls, filename: str, encoding: str="utf-8"):
        """
        Read a file and exit the program on failure.

        Attempts to read the contents of the given file using `cls.read`.
        If an error occurs (e.g., file not found, permission denied, or
        encoding issues), the exception is printed to stderr and the
        program terminates with `sys.exit(ECODE.BAD)`.

        Parameters
        ----------
        filename : str
            Path to the file to be read.
        encoding : str, default "utf-8"
            Text encoding used to open the file.

        Returns
        -------
        str
            The file contents as a string if reading succeeds.

        Raises
        ------
        Exception
            Always raised if any exception occurs while reading the file.
            The exit code is `ECODE.BAD`.

        Notes
        -----
        - This method is intended for command-line tools or scripts where
          failure to read a file should immediately terminate execution.
        - For safer error handling without exiting, use `FileUtils.read`
          directly instead.
        """
        try:
            content = cls.read(filename, encoding=encoding)
            return content
        except Exception as ex:
            print(f'*** {type(ex).__name__}: {ex}')
            sys.exit(ECODE.BAD)

    @classmethod
    def write(cls, filename: str, content: str, encoding: str="utf-8"):
        """
        Write text content to a file.

        This method opens the specified file in write mode using
        `get_file_stream`, writes the provided string into it, and
        returns once the operation is complete. By default, the file
        is written with UTF‑8 encoding.

        Parameters
        ----------
        filename : str
            Path to the file to write. If the file does not exist,
            it will be created. If it exists, its contents will be
            overwritten.
        content : str
            The text content to write into the file.
        encoding : str, default "utf-8"
            Text encoding used to encode the file content.

        Returns
        -------
        None
            This method performs a side effect (writing to disk) but
            does not return a value.

        Raises
        ------
        ValueError
            If `filename` is empty after normalization.
        OSError
            If the file cannot be opened or written to.

        Notes
        -----
        - The file is opened in text mode with write access (`"w"`),
          which overwrites any existing content.
        - For appending instead of overwriting, use `"a"` mode with
          `get_file_stream`.
        """
        stream = cls.get_file_stream(filename, mode="w", encoding=encoding)
        stream.write(content)

    @classmethod
    def safe_load_yaml(cls, filename: str):
        """
        Load and parse a YAML file safely.

        Reads the file contents using `cls.read`, parses them with
        `yaml.safe_load`, and returns the corresponding Python object.

        Parameters
        ----------
        filename : str
            Path to the YAML file to be loaded.

        Returns
        -------
        Any
            Parsed Python object. Typically a dict, list, scalar, or None
            depending on the YAML content.

        Raises
        ------
        ValueError
            If `filename` is empty after normalization.
        OSError
            If the file cannot be read.
        yaml.YAMLError
            If the YAML content is invalid or cannot be parsed.
        """
        stream = cls.read(filename)
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as ex:
            raise yaml.YAMLError(f"Failed to parse YAML file {filename}: {ex}")
