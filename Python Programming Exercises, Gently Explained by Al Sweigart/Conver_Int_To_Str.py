def convertIntToStr(integerNum):

    if integerNum == 0:
        return '0'

    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    if integerNum < 0:
        isNegative = True
        integerNum = -integerNum
    else:
        isNegative = False

    stringNum = ''

    while integerNum > 0:
        onesPlaceDigit = integerNum % 10
        stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
        integerNum //= 10
        
    if isNegative:
        return '-' + stringNum
    else:
        return stringNum
for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)