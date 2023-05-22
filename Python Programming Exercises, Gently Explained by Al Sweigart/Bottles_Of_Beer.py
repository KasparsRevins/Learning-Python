"""
“99 Bottles of Beer on the Wall” is a cumulative song often sung to pass the time (and annoy anyone close to the singer).
Long, tedious activities are the perfect task for computers. In this exercise, you’ll write a program to display the complete lyrics of this song.
"""
bottles = 10
while bottles > 0:
    if bottles == 1:
        print(str(bottles) + " bottle of beer on the wall,\n " + str(bottles) + " bottle of beer,\n Take one down,\n Pass it around," )
        print("No more bottles of beer on the wall!")
        break
    print(str(bottles) + " bottles of beer on the wall,\n " + str(bottles) + " bottles of beer,\n Take one down,\n Pass it around," )
    bottles -= 1