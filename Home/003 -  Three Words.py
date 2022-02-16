"""
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession . For example, the string "start 5 one two three 7 end
" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.

Example:
1. checkio("Hello World hello") == True
2. checkio("He is 123 man") == False
3. checkio("1 2 3 4") == False
4. checkio("bla bla bla bla") == True
5. checkio("Hi") == False

How it is used: This teaches you how to work with strings and introduces some useful functions.
Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100

"""


def checkio(words: str) -> bool:
    list_of_words = words.split()
    is_3_words = 0
    for word in list_of_words:
        if word.isalpha():
            is_3_words += 1
        else:
            is_3_words = 0

        if is_3_words == 3:
            break
    return True if is_3_words == 3 else False




inp = 'Hello World hello'
inp2 = 'He is 123 man'
print(checkio(inp))
print(checkio(inp2))
