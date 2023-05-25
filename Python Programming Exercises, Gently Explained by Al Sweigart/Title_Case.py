"""
In this exercise, you’ll have to convert a string to title case where every word in the string begins with an uppercase letter. 
The remaining letters in the word are in lowercase. Title case is a slight increase in complexity compared to Exercise #34, “Uppercase Letters”, 
so I advise that you solve that exercise before attempting this one.
"""

def getTitleCase(text):
    titledText = ""
    for i in range(len(text)):
        if i == 0:
            titledText += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titledText += text[i].upper()
        else:
            titledText += text[i].lower()
    return titledText

assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'