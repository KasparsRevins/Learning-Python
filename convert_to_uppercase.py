inputted_string = input("String to convert: ")
inputted_number = int(input("How many last letters should be converted ? "))

inputted_number = -abs(inputted_number)
print(inputted_number)
inputted_string = inputted_string[:inputted_number] + inputted_string[inputted_number:].upper()
print(inputted_string)  