"""
In the US and UK, the digits of numbers are grouped with commas every three digits. For example, 
the number 79033516 is written as 79,033,516 for readability. In this exercise, you’ll write a function that takes a number and returns a string of the number with comma formatting.
"""

def commaFormat(number):
    return f'{number:,}'

assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'