for x in range(0,200):
    if x == 0:
        continue
    elif x % 3 != 0:
        continue
    elif type(x) != int:
        continue
    else:
        pass
    print(x)