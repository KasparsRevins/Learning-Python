"""
Write a rot13() function with a text parameter that returns the ROT 13 encrypted version of text. 
Uppercase letters encrypt to uppercase letters and lowercase letters encrypt to lowercase letters. 
For example, 'HELLO, world!' encrypts to 'URYYB, jbeyq!' and 'hello, WORLD!' encrypts to 'uryyb, JBEYQ!
"""

def rot13(text):
    encryptedText = ''
    for character in text:
        if not character.isalpha():
            encryptedText += character 
        else:
            rotatedLetterOrdinal = ord(character) + 13
            if character.islower() and rotatedLetterOrdinal > 122:
                rotatedLetterOrdinal -= 26
            if character.isupper() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26

            encryptedText += chr(rotatedLetterOrdinal)

    return encryptedText

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'