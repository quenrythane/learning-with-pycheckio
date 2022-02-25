# https://py.checkio.org/en/mission/backward-each-word/
"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.

Example:
backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition: The line consists only from alphabetical symbols and spaces.
"""


def backward_string_by_word(text: str) -> str:
    return ' '.join(word[::-1] for word in text.split(' '))
    # it works for extra spaces, cause .split(' ') see every spaces as seperator.
    # and because we have few spaces (replace it by x for visibility) so we have something like xxx
    # and between x-es we have ''. So output of split is ['hello', '', '', '', 'world'] which help as join it all later


print(backward_string_by_word('hello world'))
print(backward_string_by_word('hello    world'))
