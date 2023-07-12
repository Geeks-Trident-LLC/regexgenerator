"""Module containing the attributes for regexpro."""

from os import path
from textwrap import dedent

from pathlib import Path
from pathlib import PurePath

import yaml

from genericlib import version as gtlib_version
from genericlib import File

__version__ = '0.3.12'
version = __version__
__edition__ = 'Pro'
edition = __edition__

__all__ = [
    'version',
    'edition',
    'Data'
]


class Data:
    # app yaml files
    system_reference_filename = str(
        PurePath(
            Path(__file__).parent,
            'system_references.yaml'
        )
    )
    symbol_reference_filename = str(
        PurePath(
            Path(__file__).parent,
            'symbols.yaml'
        )
    )
    user_reference_filename = str(
        PurePath(
            Path.home(),
            '.geekstrident',
            'regexpro',
            'user_references.yaml'
        )
    )

    # main app
    main_app_text = f'RegexApp v{version}'

    # packages
    pyyaml_text = f'pyyaml v{yaml.__version__}'
    pyyaml_link = 'https://pypi.org/project/PyYAML/'

    gtgenlib_text = f"genericlib v{gtlib_version}"
    gtgenlib_link = ""

    # company
    company = 'Geeks Trident LLC'
    company_full_name = company
    company_name = "Geeks Trident"
    company_url = 'https://www.geekstrident.com/'

    # URL
    repo_url = 'https://github.com/Geeks-Trident-LLC/regexpro'
    documentation_url = path.join(repo_url, 'blob/develop/README.md')
    license_url = path.join(repo_url, 'blob/develop/LICENSE')

    # License
    years = '2022'
    license_name = f'{company_name} License'
    copyright_text = f'Copyright \xa9 {years}'
    license = dedent(
        f"""
        {company_name} License

        {copyright_text} {company}.  All rights reserved.

        Unauthorized copying of file, source, and binary forms without {company_name} permissions, via any medium is strictly prohibited.

        Proprietary and confidential.

        Written by Tuyen Mathew Duong <tuyen@geekstrident.com>, Jan 14, 2022.
        """).strip()

    @classmethod
    def get_dependency(cls):
        dependencies = dict(
            pyyaml=dict(
                package=cls.pyyaml_text,
                url=cls.pyyaml_link
            ),
            gtgenlib=dict(
                package=cls.gtgenlib_text,
                url=""
            )
        )
        return dependencies

    @classmethod
    def get_app_keywords(cls):
        with open(cls.system_reference_filename) as stream:
            content = stream.read()
            return content

    @classmethod
    def get_defined_symbols(cls):
        with open(cls.symbol_reference_filename) as stream:
            content = stream.read()
            return content

    @classmethod
    def get_user_custom_keywords(cls):
        filename = cls.user_reference_filename
        if not File.is_exist(filename):
            File.create(cls.user_reference_filename)
            content = dedent("""
            ###########################################################
            # These custom keywords are created by various end-users. #
            # Ask maintainer to add new custom keyword.               #
            # Geeks Trident has NO LICENSE RIGHT to these keywords.   #
            ###########################################################
            
            regex_word: &regex_word
              author: Tuyen M Duong <tuyen@geekstrident.com> -- 2023-07-12
              description: a pattern to match a word or underline mark.
              pattern: "\\w+"
              positive_test: ["abc", "xyz", "abc_xyz", "a123", "_____"]
              negative_test: ["!@-+", "   "]
            
            rword: *regex_word
            
            regex_word_or_group: &regex_word_or_group
              author: Tuyen M Duong <tuyen@geekstrident.com> -- 2023-07-12
              description: a pattern to match at least one word or underline mark.
              pattern: "\\w+( \\w+)*"
              positive_test: ["abc", "abc xyz", "xyz abc_xyz", "a123 _____ xyz"]
              negative_test: ["!@-+", "+++ ---"]
            
            regex_words: *regex_word_or_group
            
            rwords: *regex_word_or_group
            
            regex_word_or_flex_group: &regex_word_or_flex_group
              author: Tuyen M Duong <tuyen@geekstrident.com> -- 2023-07-12
              description: a pattern to match at least one word or underline mark.
              pattern: "\\w+( +\\w+)*"
              positive_test: ["abc", "abc xyz", "xyz   abc_xyz", "a123   _____ xyz"]
              negative_test: ["!@-+", "+++ ---"]
            
            flex_regex_words: *regex_word_or_flex_group
            
            flex_rwords: *regex_word_or_flex_group
            
            regex_word_group: &regex_word_group
              author: Tuyen M Duong <tuyen@geekstrident.com> -- 2023-07-12
              description: a pattern to match at least two words or underline mark.
              pattern: "\\w+( \\w+)+"
              positive_test: ["abc xyz", "xyz abc_xyz", "a123 _____ xyz"]
              negative_test: ["!@-+", "+++ ---", "abc"]
            
            rword_group: *regex_word_group
            
            regex_word_flex_group: &regex_word_flex_group
              author: Tuyen M Duong <tuyen@geekstrident.com> -- 2023-07-12
              description: a pattern to match at least two words or underline mark.
              pattern: "\\w+( +\\w+)+"
              positive_test: ["abc xyz", "xyz   abc_xyz", "a123 _____   xyz"]
              negative_test: ["!@-+", "+++ ---", "abc"]
            
            rword_flex_group: *regex_word_flex_group
            
            """).lstrip()

            File.save(filename, content)

        with open(filename) as stream:
            content = stream.read()
            return content
