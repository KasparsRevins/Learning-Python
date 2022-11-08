password = "random"
correct = False
while correct == False:
    answer = input("Please enter your password: ")
    if answer == password:
        print("Welcome back user!")
        correct = True
    else:
        print("Invalid password, try again...")