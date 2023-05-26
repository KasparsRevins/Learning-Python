"""
One of the most efficient sorting algorithms is the merge sort algorithm. Merge sort has two phases: the dividing phase and the merge phase. 
We won’t dive into this advanced algorithm in this book. However, we can write code for the second half: merging two pre-sorted lists of integers into a single sorted list.
Write a mergeTwoLists() function with two parameters list1 and list2. The lists of numbers passed for these parameters are already in sorted order from smallest to largest number. 
The function returns a single sorted list of all numbers from these two lists.
"""

def mergeTwoLists(list1,list2):
    unsorted_list = list1 + list2
    sorted_list = []

    while unsorted_list:
        minimum = unsorted_list[0]
        for item in unsorted_list:
            if item < minimum:
                minimum = item
        sorted_list.append(minimum)
        unsorted_list.remove(minimum)

    return sorted_list


assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]

assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]

assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
