"""
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.

Input: A string.
Output: A string.

Example:
1. first_word("Hello world") == "Hello"
2. first_word("greetings, friends") == "greetings"

How it is used: the first word is a command in a command line
Precondition: the text can contain a-z A-Z , . '
"""


def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').split()
    return text[0]


inp = "Hello world"
print(first_word(inp))
