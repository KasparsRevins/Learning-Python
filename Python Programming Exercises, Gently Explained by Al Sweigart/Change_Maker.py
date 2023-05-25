"""
American currency has coins in the denominations of 1 (pennies), 5 (nickels), 10 (dimes), and 25 cents (quarters). 
Imagine that we were programming a cash register to dispense correct change. In this exercise, we would need to calculate the number of each coin for a given amount of change.
"""


def makeChange(amount):
    change = {}

    if amount >= 25:
        change['quarters'] = amount // 25
        amount = amount % 25

    if amount >= 10:
        change['dimes'] = amount // 10
        amount = amount % 10

    if amount >= 5:
        change['nickels'] = amount // 5
        amount = amount % 5

    if amount >= 1:
        change["pennies"] = amount
        
    return change


assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}