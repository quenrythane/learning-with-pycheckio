# https://py.checkio.org/en/mission/sort-array-by-element-frequency/
"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they
 appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable

Example:
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

Precondition: elements can be ints or strings
The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""


def frequency_sort(items):
    counter = {}
    for i in items:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    result = []
    [[result.append(k) for i in range(v)] for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True)]
    return result


print('result', frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
print('result', frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']))
