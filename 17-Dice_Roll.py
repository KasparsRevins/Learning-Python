
"""
This exercise uses Python’s random number generating functions to simulate rolling any number of six-sided dice and returning the total sum of the dice roll. 
This exercise covers random number generation with Python’s random module.

Exercise Description

Write a rollDice() function with a numberOfDice parameter that represents the number of six-sided dice. 
The function returns the sum of all of the dice rolls. For this exercise you must import Python’s random module to call its random.randint() function for this exercise.
"""

def rollDice(numberOfDice):
    import random
    result = 0
    for number in range(numberOfDice):
        result += random.randint(1,6)
    return result

assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600