
"""
While cardinal numbers refer to the size of a group of objects like “four apples” or “1,000 tickets”, ordinal numbers refer to the place of an object in an ordered sequence like “first place” or “30th birthday”.
This exercise involves numbers but is more an exercise in processing text than doing math.

Exercise Description

In English, ordinal numerals have suffixes such as the “th” in “30th” or “nd” in “2nd”. Write an ordinalSuffix() function with an integer parameter named number and returns a string of the number with its ordinal suffix. For example, ordinalSuffix(42) should return the string '42nd'.

You may use Python’s str() function to convert the integer argument to a string. Python’s endswith() string method could be useful for this exercise, but to maintain the challenge in this exercise, don’t use it as part of your solution.
"""

def ordinalSuffix(number):
    numberStr = str(number)
    if numberStr[-2:] in ("11", "12", "13"):
        return numberStr + "th"
    if numberStr[-1] == "1":
        return numberStr + "st"
    if numberStr[-1] == "2":
        return numberStr + "nd"
    if numberStr[-1] == "3":
        return numberStr + "rd"

    return numberStr + "th"
    
assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'