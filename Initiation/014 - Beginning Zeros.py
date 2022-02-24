# https://py.checkio.org/en/mission/beginning-zeros/
"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.

Example:
beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4

Precondition: 0-9
"""


def beginning_zeros(number: str) -> int:
    for i in number:
        if i != '0':
            return number.index(i)
    return len(number)


def beginning_zeros2(number: str) -> int:
    str_int = str(int(number))
    return len(number) - len(str_int) + (str_int == '0')


def beginning_zeros3(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


print(beginning_zeros2('000'))
print(beginning_zeros3('020'))

print('taka'.rstrip('ak'))
