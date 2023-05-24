"""
Python is known as a “batteries included” language because its standard library comes with many useful functions and modules. 
One of these is the upper() string method, which returns an uppercase version of the string: 'Hello'.upper() evaluates to 'HELLO'. 
However, in this exercise, you’ll create your own implementation of this method.
"""
LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

def getUppercase(text):
    uppercaseText = ''
    for character in text:
        if character in LOWER_TO_UPPER:
            uppercaseText += LOWER_TO_UPPER[character]
        else:
            uppercaseText += character
    return uppercaseText
assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''