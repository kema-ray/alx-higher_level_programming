#!/usr/bin/python3
for a in range(0, 9):
    for i in range(a + 1, 10):
        if a == 8:
            print("{}{}".format(a,i))
        else:
            print("{}{}".format(a,i), end=", ")
