
"""
While a password made from a single English word like “rosebud” or “swordfish” is easy to remember, it isn’t secure. A dictionary attack is when hackers program their computers to repeatedly try logging in with every word in the dictionary as the password. 
A dictionary attack won’t work if you use randomly generated passwords. They may not be easy to remember, but they make hacking your accounts more difficult.

Exercise Description

Write a generatePassword() function that has a length parameter. The length parameter is an integer of how many characters the generated password should have. 
For security reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway. 
The password string returned by the function must have at least one lowercase letter, one uppercase letter, one number, and one special character. The special characters for this exercise are ~!@#$%^&*()_+.
"""


lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
specialCharacters = "~!@#$%^&*()_+"

concatenated = lowerCase + upperCase + numbers + specialCharacters

def generatePassword(length):
    import random
    if length < 12:
        length = 12

    password = []

    password.append(lowerCase[random.randint(0, 25)])
    password.append(upperCase[random.randint(0, 25)])
    password.append(numbers[random.randint(0, 9)])
    password.append(specialCharacters[random.randint(0, 12)])

    while len(password) < length:
        password.append(concatenated[random.randint(0, 74)])

    random.shuffle(password)

    concatenated.join(password)
    return password

assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in lowerCase:

        hasLowercase = True

    if character in upperCase:

        hasUppercase = True

    if character in numbers:

        hasNumber = True

    if character in concatenated:

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial