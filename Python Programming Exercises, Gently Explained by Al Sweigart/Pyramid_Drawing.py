"""
This exercise continues the generative ASCII art programs of Exercise #27, “Rectangle Drawing,” and Exercise #28, 
“Border Drawing.” In this exercise, your code prints a pyramid of hashtag characters in any given size.
"""

def drawPyramid(height):
    counter = 0
    print(("#").center(height * height))
    for i in range(height):
        counter += 1
        print(("#" + "##" * counter).center(height * height))  

drawPyramid(3)
drawPyramid(8)
drawPyramid(30)