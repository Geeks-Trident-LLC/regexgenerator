"""Top-level module for regexbuilder.

- support TextPattern, ElementPattern, LinePattern, MultilinePattern, and PatternBuilder
- support predefine pattern reference on system_references.yaml
- allow end-user to customize pattern on /home/.geekstrident/regexbuilder/user_references.yaml
- allow end-user to generate test script or pattern on GUI application.
- dynamically generate Python snippet script
- dynamically generate Python unittest script
- dynamically generate Python pytest script
"""

from regexbuilder.collection import TextPattern
from regexbuilder.collection import ElementPattern
from regexbuilder.collection import LinePattern
from regexbuilder.collection import PatternBuilder
from regexbuilder.collection import MultilinePattern
from regexbuilder.collection import PatternReference
from regexbuilder.core import RegexBuilder
from regexbuilder.core import DynamicTestScriptBuilder
from regexbuilder.core import add_reference
from regexbuilder.core import remove_reference

from regexbuilder.core import NonCommercialUseCls

from regexbuilder.config import version
from regexbuilder.config import edition
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
