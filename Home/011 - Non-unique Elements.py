# https://py.checkio.org/en/mission/non-unique-elements/
"""
If you have 50 different plug types, appliances wouldn't be available and would be very expensive. But once an electric
outlet becomes standardized, many companies can design appliances, and competition ensues, creating variety and better prices for consumers.
-- Bill Gates

You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique
 elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once).
  When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

Input: A list of integers.
Output: An iterable of integers.

Example:
checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
checkio([2]) == []

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving
more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

Precondition:
0 < len(data) < 1000
"""


def checkio(data: list) -> list:
    new_data = []
    counter = {}
    unique_items = []
    # liczę ilość powtórzeń poycji i wrzucam do słownika
    for i in data:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    # sprawdzam, czy któryś item powtarza się raz i dodaje go do listy
    for k, v in counter.items():
        if v == 1:
            unique_items.append(k)

    # przechodzę przez listę dodaje itemy do nowej listy, jeśli dany item nie jest w liczbie 1
    for i, v in enumerate(data):
        if v not in unique_items:
            new_data.append(v)

    return new_data


print(checkio([1, 2, 3, 1, 3]), " == [1, 3, 1, 3]")
