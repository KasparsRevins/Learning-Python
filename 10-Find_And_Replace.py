
"""
Find-and-replace is a standard feature in text editors, IDEs, and word processor software. Even the Python language comes with a replace() string method since programs often use it. 
In this exercise, you’ll reimplement this common string operation.

Exercise Description

Write a findAndReplace() function that has three parameters: text is the string with text to be replaced, oldText is the text to be replaced, and newText is the replacement text. 
Keep in mind that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in 'MY DOG JONESY' won’t be replaced.
"""

def findAndReplace(text, oldText, newText):
    replacedText = ""
    i = 0
    while i < len(text):
        if text[i:i + len(oldText)] == oldText:
            replacedText += newText
            i += len(oldText)
        else:
            replacedText += text[i]
            i += 1
    return replacedText


findAndReplace('The fox', 'fox', 'dog')
findAndReplace('fox', 'fox', 'dog')
findAndReplace('Firefox', 'fox', 'dog')