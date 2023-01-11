#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        den = 0
        for tup in my_list:
            number += (tup[0] * tup[1])
            den += (tup[1])
        return (number/den)
    return 0
