#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each element in the row using str.format() and ensure no trailing space
        print(" ".join("{:d}".format(x) for x in row))
 
