"""
There is only one handshake that can happen between two people. Between three people, there are three possible handshaking pairs. 
Between four people, there are six handshakes; five people, ten handshakes, and so on. This exercise explores the full range of possible handshaking combinations with nested for loops.
"""

def printHandshakes(people):
    numberOfHandshakes = 0
    for i in range(0, len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i], "shakes hands with",people[j])
            numberOfHandshakes += 1
    return numberOfHandshakes
