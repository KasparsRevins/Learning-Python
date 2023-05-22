

"""
A chess board has a checker-pattern of white and black tiles. In this program, you’ll determine a pattern to the color of the squares based on their column and row. 
This program challenges you to take a real-world object such as a chess board, determine the patterns behind its design, and translate that into Python code.

Exercise Description

Write a getChessSquareColor() function that has parameters column and row. The function either returns 'black' or 'white' depending on the color at the specified column and row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and end at 7 like in Figure 9-1. 
If the arguments for column or row are outside the 0 to 7 range, the function returns a blank string.
"""

def getChessSquareColor(column, row):
    if column or row > 7 or column or row < 0:
        print("")
    elif column % 2 == 0 and row % 2 == 0 or column % 2 != 0 and row % 2 != 0:
        print("White")
    else:
        print("Black")
    
getChessSquareColor(0,6)