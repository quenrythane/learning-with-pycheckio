# https://py.checkio.org/en/mission/all-upper/
"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.

Example:

is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == True
is_all_upper('444') == True
is_all_upper('55 55 5') == True

Precondition: a-z, A-Z, 1-9 and spaces
"""


def is_all_upper(text: str) -> bool:
    return text.isupper()


print(is_all_upper('ALL UPPER'))
print(is_all_upper('all lower'))
