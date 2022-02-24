# https://py.checkio.org/en/mission/replace-first/
"""
In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

example

Input: List.

Output: Iterable.

Example:

replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
"""


def replace_first(items: list):
    if items:
        items.append(items.pop(0))
    return items


print(replace_first([1,2,3,4]))
print(replace_first([1]))
print(replace_first([]))

