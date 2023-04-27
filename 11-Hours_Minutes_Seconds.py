
"""
Websites often use relative timestamps such as “3 days ago” or “about 3h ago” so the user doesn’t need to compare an absolute timestamp to the current time. 
In this exercise, you write a function that converts a number of seconds into a string with the number of hours, minutes, and seconds.

Exercise Description

Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The argument for this parameter will be the number of seconds to be translated into the number of hours, minutes, and seconds. 
If the amount for the hours, minutes, or seconds is zero, don’t show it: the function should return '10m' rather than '0h 10m 0s'. 
The only exception is that getHoursMinutesSeconds(0) should return '0s'.
"""


def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return '0s'

    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600

    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60

    seconds = totalSeconds

    hms = []
    if hours > 0:
        hms.append(str(hours) + 'h')
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    if seconds > 0:
        hms.append(str(seconds) + 's')

    return ' '.join(hms)