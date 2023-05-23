"""
Similar to the solid, filled-in ASCII art rectangles our code generated in Exercise #27, 
“Rectangle Drawing,” this exercise draws only the border of a rectangle. The + plus character is used for the corners,
the - dash character for horizontal lines, and the | pipe character for vertical lines.
"""

def drawBorder(width,height):
    counter = 0
    if width < 2 or height < 2:
        return
    while True:
        counter +=1
        if height == counter:
            unedited_line = "— " * width
            edited_line = "+" + unedited_line[1:-2] + "+"
            print(edited_line)
            break
        if counter == 1:
            unedited_line = "— " * width
            edited_line = "+" + unedited_line[1:-2] + "+"
            print(edited_line)
        if height !=0:
            unedited_middle_line = "  " * width
            edited_middle_line = "|" + unedited_middle_line[1:-2] + "|"
            print(edited_middle_line)
drawBorder(16,4)