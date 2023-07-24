import pytest       # noqa
import re
from regexpro import ElementPattern


class TestElementPattern:
    @pytest.mark.parametrize(
        ('data', 'expected_result'),
        [
            ####################################################################
            # predefined keyword test                                          #
            ####################################################################
            ('anything()', '.'),
            ('something()', '.*'),
            ('everything()', '.+'),
            ('space()', ' '),
            ('spaces()', ' +'),
            ('non_space()', '[^ ]'),
            ('non_spaces()', '[^ ]+'),
            ('whitespace()', '\\s'),
            ('whitespaces()', '\\s+'),
            ('non_whitespace()', '\\S'),
            ('non_whitespaces()', '\\S+'),
            ('punctuation()', r'[!\"#$%&\'()*+,./:;<=>?@\[\\\]\^_`{|}~-]'),
            ('punctuations()', r'[!\"#$%&\'()*+,./:;<=>?@\[\\\]\^_`{|}~-]+'),
            ('non_punctuation()', r'[^!\"#$%&\'()*+,./:;<=>?@\[\\\]\^_`{|}~-]'),
            ('non_punctuations()', r'[^!\"#$%&\'()*+,./:;<=>?@\[\\\]\^_`{|}~-]+'),
            ('letter()', '[a-zA-Z]'),
            ('letters()', '[a-zA-Z]+'),
            ('word()', '[a-zA-Z0-9]+'),
            ('words()', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)*'),
            ('mixed_word()', '[\\x21-\\x7e]+'),
            ('mixed_words()', '[\\x21-\\x7e]+( [\\x21-\\x7e]+)*'),
            ('phrase()', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)+'),
            ('mixed_phrase()', '[\\x21-\\x7e]+( [\\x21-\\x7e]+)+'),
            ('hexadecimal()', '[0-9a-fA-F]'),
            ('hex()', '[0-9a-fA-F]'),
            ('octal()', '[0-7]'),
            ('binary()', '[01]'),
            ('digit()', '\\d'),
            ('digits()', '\\d+'),
            ('number()', '(\\d+)?[.]?\\d+'),
            ('signed_number()', '[+(-]?(\\d+)?[.]?\\d+[)]?'),
            ('mixed_number()', '[+\\(\\[\\$-]?(\\d+(,\\d+)*)?[.]?\\d+[\\]\\)%a-zA-Z]*'),
            # ('datetime()', '\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}:\\d{2}'),
            # ('datetime(format)', '\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}:\\d{2}'),
            # ('datetime(format1)', '\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2}'),
            # ('datetime(format1, format3)', '(([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+)|([a-zA-Z]+, [a-zA-Z]+ +[0-9]+, [0-9]+ [0-9]+:[0-9]+:[0-9]+ [a-zA-Z]+))'),      # noqa
            # ('datetime(var_datetime, format1, format3)', '(?P<datetime>([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+)|([a-zA-Z]+, [a-zA-Z]+ +[0-9]+, [0-9]+ [0-9]+:[0-9]+:[0-9]+ [a-zA-Z]+))'),    # noqa
            # ('datetime(var_datetime, format1, format3, n/a)', '(?P<datetime>([0-9]+/[0-9]+/[0-9]+ [0-9]+:[0-9]+:[0-9]+)|([a-zA-Z]+, [a-zA-Z]+ +[0-9]+, [0-9]+ [0-9]+:[0-9]+:[0-9]+ [a-zA-Z]+)|n/a)'),   # noqa
            ('mac_address()', '([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5})|([0-9a-fA-F]{2}(-[0-9a-fA-F]{2}){5})|([0-9a-fA-F]{2}( [0-9a-fA-F]{2}){5})|([0-9a-fA-F]{4}([.][0-9a-fA-F]{4}){2})'),     # noqa
            ('mac_address(or_n/a)', '(([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5})|([0-9a-fA-F]{2}(-[0-9a-fA-F]{2}){5})|([0-9a-fA-F]{2}( [0-9a-fA-F]{2}){5})|([0-9a-fA-F]{4}([.][0-9a-fA-F]{4}){2})|n/a)'),     # noqa
            ('mac_address(var_mac_addr, or_n/a)', '(?P<mac_addr>([0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5})|([0-9a-fA-F]{2}(-[0-9a-fA-F]{2}){5})|([0-9a-fA-F]{2}( [0-9a-fA-F]{2}){5})|([0-9a-fA-F]{4}([.][0-9a-fA-F]{4}){2})|n/a)'),   # noqa
            ('ipv4_address()', '((25[0-5])|(2[0-4]\\d)|(1\\d\\d)|([1-9]?\\d))(\\.((25[0-5])|(2[0-4]\\d)|(1\\d\\d)|([1-9]?\\d))){3}'),   # noqa
            ('ipv6_address()', '(([a-fA-F0-9]{1,4}(:[a-fA-F0-9]{1,4}){5})|([a-fA-F0-9]{1,4}:(:[a-fA-F0-9]{1,4}){1,4})|(([a-fA-F0-9]{1,4}:){1,2}(:[a-fA-F0-9]{1,4}){1,3})|(([a-fA-F0-9]{1,4}:){1,3}(:[a-fA-F0-9]{1,4}){1,2})|(([a-fA-F0-9]{1,4}:){1,4}:[a-fA-F0-9]{1,4})|(([a-fA-F0-9]{1,4}:){1,4}:)|(:(:[a-fA-F0-9]{1,4}){1,4}))'),     # noqa
            ('interface()', '[a-zA-Z][a-zA-Z0-9_/.-]*[0-9]'),
            ('version()', '[0-9]\\S*'),
            ####################################################################
            # predefined keyword test combining with other flags               #
            ####################################################################
            ('word(var_v1, or_empty)', '(?P<v1>[a-zA-Z0-9]+|)'),
            ('word(var_v1, or_n/a, or_empty)', '(?P<v1>[a-zA-Z0-9]+|n/a|)'),
            ('word(var_v1, or_abc xyz, or_12.95 19.95, or_empty)', '(?P<v1>[a-zA-Z0-9]+|(abc xyz)|(12.95 19.95)|)'),
            ('word(var_v1, word_bound_left)', '(?P<v1>\\b[a-zA-Z0-9]+)'),
            ('word(var_v1, word_bound_right)', '(?P<v1>[a-zA-Z0-9]+\\b)'),
            ('word(var_v1, word_bound)', '(?P<v1>\\b[a-zA-Z0-9]+\\b)'),
            ('word(var_v1, word_bound_raw)', '(?P<v1>[a-zA-Z0-9]+|word_bound)'),
            ('word(var_v1, head)', '^(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_ws)', '^\\s*(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_ws_plus)', '^\\s+(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_whitespace)', '^\\s*(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_whitespace_plus)', '^\\s+(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_whitespaces)', '^\\s+(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_space)', '^ *(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_space_plus)', '^ +(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_spaces)', '^ +(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_ws)', '\\s*(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_ws_plus)', '\\s+(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_whitespace)', '\\s*(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_whitespace_plus)', '\\s+(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_whitespaces)', '\\s+(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_space)', ' *(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_space_plus)', ' +(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_just_spaces)', ' +(?P<v1>[a-zA-Z0-9]+)'),
            ('word(var_v1, head_raw)', '(?P<v1>[a-zA-Z0-9]+|head)'),
            ('word(var_v1, tail)', '(?P<v1>[a-zA-Z0-9]+)$'),
            ('word(var_v1, tail_ws)', '(?P<v1>[a-zA-Z0-9]+)\\s*$'),
            ('word(var_v1, tail_ws_plus)', '(?P<v1>[a-zA-Z0-9]+)\\s+$'),
            ('word(var_v1, tail_whitespace)', '(?P<v1>[a-zA-Z0-9]+)\\s*$'),
            ('word(var_v1, tail_whitespace_plus)', '(?P<v1>[a-zA-Z0-9]+)\\s+$'),
            ('word(var_v1, tail_whitespaces)', '(?P<v1>[a-zA-Z0-9]+)\\s+$'),
            ('word(var_v1, tail_space)', '(?P<v1>[a-zA-Z0-9]+) *$'),
            ('word(var_v1, tail_space_plus)', '(?P<v1>[a-zA-Z0-9]+) +$'),
            ('word(var_v1, tail_spaces)', '(?P<v1>[a-zA-Z0-9]+) +$'),
            ('word(var_v1, tail_just_ws)', '(?P<v1>[a-zA-Z0-9]+)\\s*'),
            ('word(var_v1, tail_just_ws_plus)', '(?P<v1>[a-zA-Z0-9]+)\\s+'),
            ('word(var_v1, tail_just_whitespace)', '(?P<v1>[a-zA-Z0-9]+)\\s*'),
            ('word(var_v1, tail_just_whitespace_plus)', '(?P<v1>[a-zA-Z0-9]+)\\s+'),
            ('word(var_v1, tail_just_whitespaces)', '(?P<v1>[a-zA-Z0-9]+)\\s+'),
            ('word(var_v1, tail_just_space)', '(?P<v1>[a-zA-Z0-9]+) *'),
            ('word(var_v1, tail_just_space_plus)', '(?P<v1>[a-zA-Z0-9]+) +'),
            ('word(var_v1, tail_just_spaces)', '(?P<v1>[a-zA-Z0-9]+) +'),
            ('word(var_v1, tail_raw)', '(?P<v1>[a-zA-Z0-9]+|tail)'),
            ('letter(var_word, repetition_3)', '(?P<word>[a-zA-Z]{3})'),
            ('letter(var_word, repetition_3_8)', '(?P<word>[a-zA-Z]{3,8})'),
            ('letter(var_word, repetition_3_)', '(?P<word>[a-zA-Z]{3,})'),
            ('letter(var_word, repetition__8)', '(?P<word>[a-zA-Z]{,8})'),
            ('word(var_v1, N/A, repetition_3, word_bound)', '(?P<v1>\\b(([a-zA-Z0-9]+){3}|N/A)\\b)'),
            ('letter(0_or_1_occurrence)', '[a-zA-Z]?'),
            ('letter(0_or_more_occurrence)', '[a-zA-Z]*'),
            ('letter(1_or_more_occurrence)', '[a-zA-Z]+'),
            ('letter(3_or_more_occurrence)', '[a-zA-Z]{3,}'),
            ('letter(at_least_0_occurrence)', '[a-zA-Z]*'),
            ('letter(at_least_1_occurrence)', '[a-zA-Z]{1,}'),
            ('letter(at_least_3_occurrence)', '[a-zA-Z]{3,}'),
            ('letter(at_most_0_occurrence)', '[a-zA-Z]?'),
            ('letter(at_most_1_occurrence)', '[a-zA-Z]{,1}'),
            ('letter(at_most_3_occurrence)', '[a-zA-Z]{,3}'),
            ('letter(0_occurrence)', '[a-zA-Z]?'),
            ('letter(1_occurrence)', '[a-zA-Z]'),
            ('letter(3_occurrence)', '[a-zA-Z]{3}'),
            ('word(0_or_1_occurrence)', '([a-zA-Z0-9]+)?'),
            ('word(var_v1, 0_or_1_occurrence)', '(?P<v1>([a-zA-Z0-9]+)?)'),
            ('word(var_v1, 0_or_1_occurrence, N/A)', '(?P<v1>([a-zA-Z0-9]+)?|N/A)'),
            ('word(0_or_1_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)?'),
            ('word(0_or_more_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)*'),
            ('word(1_or_more_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)+'),
            ('word(3_or_more_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){3,}'),
            ('word(at_least_0_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)*'),
            ('word(at_least_1_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){1,}'),
            ('word(at_least_3_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){3,}'),
            ('word(at_most_0_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)?'),
            ('word(at_most_1_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){,1}'),
            ('word(at_most_3_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){,3}'),
            ('word(0_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)?'),
            ('word(1_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)'),
            ('word(3_phrase_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){3}'),
            ('word(0_or_1_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)?'),
            ('word(0_or_more_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)*'),
            ('word(1_or_more_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)+'),
            ('word(3_or_more_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){3,}'),
            ('word(at_least_0_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)*'),
            ('word(at_least_1_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){1,}'),
            ('word(at_least_3_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){3,}'),
            ('word(at_most_0_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)?'),
            ('word(at_most_1_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){,1}'),
            ('word(at_most_3_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){,3}'),
            ('word(0_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)?'),
            ('word(1_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+)'),
            ('word(3_group_occurrence)', '[a-zA-Z0-9]+( [a-zA-Z0-9]+){3}'),
            ####################################################################
            # alternative or_ for repeating or occurring space                 #
            ####################################################################
            ('word(var_v1, or_repeating_5_space)', '(?P<v1>( {5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_repeat_5_spaces)', '(?P<v1>( {5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_repeats_5_spaces)', '(?P<v1>( {5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_repeating_2_5_spaces)', '(?P<v1>( {2,5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_repeating__5_spaces)', '(?P<v1>( {,5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_at_least_5_spaces)', '(?P<v1>( {5,})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_at_most_5_spaces)', '(?P<v1>( {,5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_5_spaces)', '(?P<v1>( {5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_at_least_5_occurrences_spaces)', '(?P<v1>( {5,})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_at_most_5_occurrences_spaces)', '(?P<v1>( {,5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_5_occurrences_spaces)', '(?P<v1>( {5})|([a-zA-Z0-9]+))'),
            ('word(var_v1, or_either_repeating_2_5_spaces)', '(?P<v1>( {2,5})|( *[a-zA-Z0-9]+ *))'),
            ('word(var_v1, or_either_at_least_5_occurrences_spaces)', '(?P<v1>( {5,})|( *[a-zA-Z0-9]+ *))'),
            ('word(var_v1, or_either_at_most_5_occurrences_spaces)', '(?P<v1>( {,5})|( *[a-zA-Z0-9]+ *))'),
            ####################################################################
            # choice keyword test                                              #
            ####################################################################
            ('choice(up, down, administratively down)', '(up|down|(administratively down))'),
            ('choice(up, down, administratively down, var_v2)', '(?P<v2>up|down|(administratively down))'),
            ('choice(up, down, administratively down, var_v2, or_empty)', '(?P<v2>up|down|(administratively down)|)'),
            ('choice(up, down, administratively down, var_v2, or_empty, or_digits)', '(?P<v2>up|down|(administratively down)|\\d+|)'),      # noqa
            ('choice(abc, word_bound)', '\\b(abc)\\b'),
            ('choice(abc, xyz, word_bound)', '\\b(abc|xyz)\\b'),
            ('choice(var_v1, abc, xyz, word_bound)', '(?P<v1>\\b(abc|xyz)\\b)'),
            ####################################################################
            # data keyword test                                                #
            ####################################################################
            ('data(->)', '->'),
            ('data(->, or_empty)', '(->|)'),
            ####################################################################
            # symbol keyword test                                              #
            ####################################################################
            ('symbol(name=hyphen)', '-'),
            ('symbol(name=hyphen, 3_or_more_occurrence)', '-{3,}'),
            ('symbol(name=question_mark, 3_or_more_occurrence)', '\\?{3,}'),
            ('symbol(name=hexadecimal, 1_or_2_occurrence)', '[0-9a-fA-F]{1,2}'),
            ('symbol(var_v1, name=hexadecimal, 1_or_2_occurrence)', '(?P<v1>[0-9a-fA-F]{1,2})'),
            ('symbol(var_v1, name=hex, 1_or_2_occurrence, word_bound)', '(?P<v1>\\b[0-9a-fA-F]{1,2}\\b)'),
            ('symbol(var_v1, name=hex, 1_or_2_occurrence, word_bound, N/A)', '(?P<v1>\\b([0-9a-fA-F]{1,2}|N/A)\\b)'),
            ####################################################################
            # start keyword test                                               #
            ####################################################################
            ('start()', '^'),
            ('start(space)', '^ *'),
            ('start(spaces)', '^ +'),
            ('start(space_plus)', '^ +'),
            ('start(ws)', '^\\s*'),
            ('start(ws_plus)', '^\\s+'),
            ('start(whitespace)', '^\\s*'),
            ('start(whitespaces)', '^\\s+'),
            ('start(whitespace_plus)', '^\\s+'),
            ####################################################################
            # end keyword test                                               #
            ####################################################################
            ('end()', '$'),
            ('end(space)', ' *$'),
            ('end(spaces)', ' +$'),
            ('end(space_plus)', ' +$'),
            ('end(ws)', '\\s*$'),
            ('end(ws_plus)', '\\s+$'),
            ('end(whitespace)', '\\s*$'),
            ('end(whitespaces)', '\\s+$'),
            ('end(whitespace_plus)', '\\s+$'),
            ####################################################################
            # raw data test                                                    #
            ####################################################################
            ('word(raw>>>)', 'word\\(\\)'),
            ('word(raw>>>data="")', 'word\\(data=""\\)'),
            ####################################################################
            # unknown keyword test                                             #
            ####################################################################
            ('abc_word()', 'abc_word\\(\\)'),
            ('xyz_word()', 'xyz_word\\(\\)'),
        ]
    )
    def test_element_pattern(self, data, expected_result):
        pattern = ElementPattern(data)
        assert pattern == expected_result
        try:
            re.compile(pattern)
        except Exception as ex:
            error = 'invalid pattern: %r (err-msg: %s)' % (pattern, ex)
            assert False, error

    @pytest.mark.parametrize(
        ('data', 'expected_result'),
        [
            ####################################################################
            # predefined keyword test                                          #
            ####################################################################
            ('datetime()', '\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}:\\d{2}'),
            ('datetime(format)', '\\d{2}/\\d{2}/\\d{4} \\d{2}:\\d{2}:\\d{2}'),
            ('datetime(format1)', '\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2}'),
            ('datetime(format1, format3)', '((\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2})|([a-zA-Z]{6,9}, [a-zA-Z]{3,9} +\\d{1,2}, \\d{4} 1?\\d:\\d{2}:\\d{2} [apAP][mM]))'),      # noqa
            ('datetime(var_datetime, format1, format3)', '(?P<datetime>(\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2})|([a-zA-Z]{6,9}, [a-zA-Z]{3,9} +\\d{1,2}, \\d{4} 1?\\d:\\d{2}:\\d{2} [apAP][mM]))'),    # noqa
            ('datetime(var_datetime, format1, format3, n/a)', '(?P<datetime>(\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}:\\d{2})|([a-zA-Z]{6,9}, [a-zA-Z]{3,9} +\\d{1,2}, \\d{4} 1?\\d:\\d{2}:\\d{2} [apAP][mM])|n/a)'),   # noqa
        ]
    )
    def test_element_pattern(self, data, expected_result):
        pattern = ElementPattern(data)
        assert pattern == expected_result
        try:
            re.compile(pattern)
        except Exception as ex:
            error = 'invalid pattern: %r (err-msg: %s)' % (pattern, ex)
            assert False, error

    @pytest.mark.parametrize(
        (
            'data', 'expected_pattern', 'expected_pattern_after_removed'
        ),
        [
            (
                'words(head)',
                '^[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*',
                '[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*'
            ),
            (
                'words(var_v1, head_whitespace)',
                '^\\s*(?P<v1>[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*)',
                '(?P<v1>[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*)'
            ),
        ]
    )
    def test_remove_head_of_pattern(self, data, expected_pattern,
                                    expected_pattern_after_removed):
        pattern = ElementPattern(data)
        assert pattern == expected_pattern

        removed_head_of_str_pattern = pattern.remove_head_of_string()
        assert removed_head_of_str_pattern == expected_pattern_after_removed

    @pytest.mark.parametrize(
        (
            'data', 'expected_pattern', 'expected_pattern_after_removed'
        ),
        [
            (
                'words(tail)',
                '[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*$',
                '[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*'
            ),
            (
                'words(var_v1, tail_whitespace)',
                '(?P<v1>[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*)\\s*$',
                '(?P<v1>[a-zA-Z][a-zA-Z0-9]*( [a-zA-Z][a-zA-Z0-9]*)*)'
            ),
        ]
    )
    def test_remove_tail_of_pattern(self, data, expected_pattern,
                                    expected_pattern_after_removed):
        pattern = ElementPattern(data)
        assert pattern == expected_pattern

        removed_tail_of_str_pattern = pattern.remove_tail_of_string()
        assert removed_tail_of_str_pattern == expected_pattern_after_removed
