# https://py.checkio.org/en/mission/acceptable-password-i/

"""
You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == True

How it’s used: For a password verification form. Also it’s good to learn how the task can be evaluated
"""


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


print(is_acceptable_password('123456a'))
