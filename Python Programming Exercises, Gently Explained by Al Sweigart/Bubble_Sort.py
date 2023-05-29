"""
Write a bubbleSort() function with a list parameter named numbers. 
The function rearranges the values in this list in-place. The function also returns the now-sorted list. 
There are many sorting algorithms, but this exercise asks you to implement the bubble sort algorithm.
"""
def bubbleSort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers
assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]


import random
x = [random.randint(1, 10000) for x in range(100)]
assert bubbleSort(x) == sorted(x)