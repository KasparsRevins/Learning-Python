"""
Clocks have an unusual counting system compared to the normal decimal number system we’re familiar with. Instead of beginning at 0 and going to 1, 2, and so on forever,
clocks start at 12 and go on to 1, 2, and so on up to 11. Then it loops back to 12 again. 
(Clocks are quite odd if you think about it: 12 am comes before 11 am and 12 pm comes before 11 pm.) 
This is a bit more complicated than simply writing a program that counts upward. This exercise requires using nested for loops to loop over the minutes, the hours, and the am and pm halve of the day.
"""


for meridiem in ["am","pm"]:
    for hours in ["12","1","2","3","4","5","6","7","8","9","10","11"]:
        for minutes in ["00","15","30","45"]:
            print(meridiem + ":" + hours + " " + minutes)