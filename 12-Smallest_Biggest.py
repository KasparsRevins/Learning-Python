
"""
Python’s built-in min() and max() functions return the smallest and biggest numbers in a list of numbers passed, respectively. In this exercise, you’ll reimplement the behavior of these functions.

This is the sort of problem that is trivial for a human to solve by hand if the list of numbers is short. 
However, if the list contains thousands, millions, or billions of numbers, you’ll need to program a computer to perform the calculation.

Exercise Description

Write a getSmallest() function that has a numbers parameter. The numbers parameter will be a list of integer and floating-point number values. The function returns the smallest value in the list. 
If the list is empty, the function should return None. Since this function replicates Python’s min() function, your solution shouldn’t use it.
"""

def smallestNumber(N):
 
    print((N % 9 + 1) * pow(10, (N // 9)) - 1)

smallestNumber(19)

def getBiggest(n):
    n.sort()
    if not n:
        return None
    else:
        return(n[-1])

getBiggest([1, 2, 3, 4, 5, 6, 7, 8, 9])