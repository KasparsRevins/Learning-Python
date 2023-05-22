"""
In this exercise, you’ll create some ASCII art, primitive graphics created from text characters. 
There will be a few such exercises in this book. In this first one, your code draws a solid rectangle out of # hashtag characters.
"""
def drawRectangle(width,height):
    for x in range(height):
        print("#" * width ,"\n", end="")

drawRectangle(10,4)