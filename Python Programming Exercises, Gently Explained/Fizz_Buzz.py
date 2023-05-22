
"""
Fizz buzz is a word game you can implement as a simple program. 
It became famous as a screening question in coding interviews to quickly determine if candidates had any programming ability whatsoever, so being able to solve it quickly leads to a good first impression.

This exercise continues our use of the modulo operator to determine if numbers are divisible by 3, 5, or both 3 and 5. “Divisible by n” means that it can be divided by a number n with no remainder. 
For example, 10 is divisible by 5, but 11 is not divisible by 5.
"""

def fizzBuzz(upTo):
    for number in range(1, upTo + 1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        elif number % 3 == 0:
            print('Fizz', end=' ')
        elif number % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(number, end=' ')