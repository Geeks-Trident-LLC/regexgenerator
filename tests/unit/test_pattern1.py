import pytest       # noqa
from regexpro import ElementPattern
import string
import re


class TestPunctuationPattern:
    def test_punctuation_pattern(self):
        pattern = ElementPattern('punctuation()')
        for p_char in string.punctuation:
            assert re.match(f'{pattern}$', p_char)

    def test_punctuations_pattern(self):
        pattern = ElementPattern('punctuations()')
        for p_char in string.punctuation:
            assert re.match(f'{pattern}$', p_char)