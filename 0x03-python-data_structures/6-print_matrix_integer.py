#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for i in range(len(a)):
            print(
                  "{:d}".format(a[i]),
                  end="" if i == len(a) - 1 else " ")
        print("")
