for i in range(1, 100 + 1):
    if i % 5 == 0:
        if i % 7 == 0:
            print(i, "бинго")
        else:
            print(i, "x5")
    elif i % 7 == 0:
        print(i, "x7")
    else:
        print(i)
