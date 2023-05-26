"""
For example, if the starting integer is 10, that number is even so the next number is 10 / 2, or 5. 5 is odd, 
so the next number is 3 × 5 + 1, or 16. 16 is even, so the next number is 8, which is even so the next number is 4, then 2, then 1. At 1, the sequence stops. 
The entire Collatz Sequence starting at 10 is: 10, 5, 16, 8, 4, 2, 1

Write a function named collatz() with a startingNumber parameter. The function returns a list of integers of the Collatz sequence that startingNumber produces. 
The first integer in this list must be startingNumber and the last integer must be 1.
"""

def collatz(startingNumber):
    list = []
    if startingNumber == 1 or startingNumber == 0:
        return list
    while True:
        if startingNumber % 2 == 0:
            list.append(startingNumber)
            startingNumber = startingNumber // 2
        if startingNumber % 2 != 0:
            list.append(startingNumber)
            if startingNumber == 1:
                return list
            startingNumber = 3 * startingNumber + 1

assert collatz(0) == []

assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]

assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

assert len(collatz(256)) == 9

assert len(collatz(257)) == 123

import random

random.seed(42)

for i in range(1000):

    startingNum = random.randint(1, 10000)

    seq = collatz(startingNum)

    assert seq[0] == startingNum # Make sure it includes the starting number.

    assert seq[-1] == 1  # Make sure the last integer is 1.