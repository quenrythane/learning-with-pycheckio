# https://py.checkio.org/en/mission/correct-sentence/
"""
For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.

Output: A string.

Example:

correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."

Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
"""


def correct_sentence(text: str) -> str:
    # return text[0].upper()+text[1:] if text[-1] == '.' else text[0].upper()+text[1:] + '.'
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


print(correct_sentence('tak'))
print(correct_sentence('Tak'))
print(correct_sentence('Tak Tak.'))
