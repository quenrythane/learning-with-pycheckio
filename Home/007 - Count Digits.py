# https://py.checkio.org/en/mission/count-digits/
"""
You need to count the number of digits in a given string.

Input: A Str.
Output: An Int.
Example:

count_digits('hi') == 0
count_digits('who is 1st here') == 1
count_digits('my numbers is 2') == 1
count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
count_digits('5 plus 6 is') == 2
count_digits('') == 0
"""


def count_digits(text: str) -> int:
    return len(["." for i in text if i.isdigit()])


def count_digits2(text: str) -> int:
    return sum(c.isdigit() for c in text)


def count_digits3(text: str) -> int:
    return sum(map(str.isdigit, text))


print(count_digits('hi12h'))
print(count_digits2('hi12h'))
print(count_digits3('hi12h'))
