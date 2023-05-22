"""
Learning the multiplication table is an early part of our childhood math education.
The multiplication table shows every product of two single digit numbers. 
In this exercise, we print a multiplication table on the screen using nested for loops and some string manipulation to align the columns correctly.
"""
print('  | 1  2  3  4  5  6  7  8  9 10')
print('--+------------------------------')
columns = 10
rows = 10
for i in range(1,rows + 1):
    print(str(i).rjust(2) + "|" ,end='')
    for j in range(1,columns + 1):
        x = i * j
        print("{:2d}".format(x), end=" ")
    print("\n")