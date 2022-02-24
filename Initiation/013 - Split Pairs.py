# https://py.checkio.org/en/mission/split-pairs/
"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.

Example:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']
1
2
Precondition: 0<=len(str)<=100
"""


def split_pairs(a: str) -> list:
    if len(a) % 2:
        a += '_'
    return [a[i-1]+a[i] for i in range(len(a)) if i % 2]


print(split_pairs('abcde'))
print(split_pairs('abcdef'))
