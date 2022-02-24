# https://py.checkio.org/en/mission/end-zeros/
"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""


def end_zeros(num: int) -> int:
    z = 0
    for n in str(num):
        if n == "0":
            z += 1
    return z


print(end_zeros(1001))
print(end_zeros(1))
