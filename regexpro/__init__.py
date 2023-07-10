"""Top-level module for regexpro.

- support TextPattern, ElementPattern, LinePattern, MultilinePattern, and PatternBuilder
- support predefine pattern reference on system_references.yaml
- allow end-user to customize pattern on /home/.geekstrident/regexpro/user_references.yaml
- allow end-user to generate test script or pattern on GUI application.
- dynamically generate Python snippet script
- dynamically generate Python unittest script
- dynamically generate Python pytest script
"""

from regexpro.collection import TextPattern
from regexpro.collection import ElementPattern
from regexpro.collection import LinePattern
from regexpro.collection import PatternBuilder
from regexpro.collection import MultilinePattern
from regexpro.collection import PatternReference
from regexpro.core import RegexBuilder
from regexpro.core import DynamicTestScriptBuilder
from regexpro.core import add_reference
from regexpro.core import remove_reference

from regexpro.core import NonCommercialUseCls

from regexpro.config import version
from regexpro.config import edition
__version__ = version
__edition__ = edition

__all__ = [
    'TextPattern',
    'ElementPattern',
    'LinePattern',
    'MultilinePattern',
    'PatternBuilder',
    'PatternReference',
    'RegexBuilder',
    'DynamicTestScriptBuilder',
    'NonCommercialUseCls',
    'add_reference',
    'remove_reference',
    'version',
    'edition',
]
