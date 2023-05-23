"""
Write a drawBox() function with a size parameter. The size parameter contains an integer for the width, length, 
and height of the box. The horizontal lines are drawn with - dash characters, the vertical lines with | 
pipe characters, and the diagonal lines with / forward slash characters. The corners of the box are drawn with + plus signs.
"""

def drawBox(size):
    if size < 1:
        return

    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

    for i in range(size - 1, -1, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

    print('+' + '-' * (size * 2) + '+')

for i in range(1, 6):
    drawBox(i)