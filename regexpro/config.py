"""Module containing the attributes for regexpro."""

from os import path
from textwrap import dedent

from pathlib import Path
from pathlib import PurePath

import yaml

__version__ = '0.3.8'
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
    main_app_text = 'RegexPro {}'.format(version)

    # packages
    pyyaml_text = 'pyyaml v{}'.format(yaml.__version__)
    pyyaml_link = 'https://pypi.org/project/PyYAML/'

    # company
    company = 'Geeks Trident LLC'
    company_url = 'https://www.geekstrident.com/'

    # URL
    repo_url = 'https://github.com/Geeks-Trident-LLC/regexpro'
    documentation_url = path.join(repo_url, 'blob/develop/README.md')
    license_url = path.join(repo_url, 'blob/develop/LICENSE')

    # License
    years = '2022-2080'
    license_name = 'Geeks Trident License'
    copyright_text = 'Copyright @ {}'.format(years)
    license = dedent(
        """
        Geeks Trident License

        Copyright (c) {}, {}
        All rights reserved.

        Unauthorized copying of file, source, and binary forms without 
        Geeks Trident permissions, via any medium is strictly prohibited.

        Proprietary and confidential.

        Written by Tuyen Mathew Duong <tuyen@geekstrident.com>, Jan 14, 2022.
        """.format(years, company)
    ).strip()

    @classmethod
    def get_dependency(cls):
        dependencies = dict(
            pyyaml=dict(
                package=cls.pyyaml_text,
                url=cls.pyyaml_link
            )
        )
        return dependencies
