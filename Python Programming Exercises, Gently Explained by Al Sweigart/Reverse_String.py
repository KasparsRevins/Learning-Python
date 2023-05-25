"""
Strings are immutable in the Python language, meaning you can’t modify their characters the way you can modify the items in a list. For example, 
if you tried to change 'Rat' to 'Ram' with the assignment statement 'Rat'[2] = 'm', you would receive a TypeError: 'str' object does not support item assignment error message. 
On the other hand, if you store a string 'Rat' in a variable named animal, the assignment statement animal = 'Ram' isn’t modifying the 'Rat' string 
but rather making animal refer to an entirely new string, 'Ram'.
"""

def reverseString(text):
    reversed_text = ""
    reversed_text = list(reversed_text)
    x = -1
    for i in range(len(text)):
        reversed_text += text[x]
        x -= 1
    reversed_text = "".join(reversed_text)
    return reversed_text
assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'