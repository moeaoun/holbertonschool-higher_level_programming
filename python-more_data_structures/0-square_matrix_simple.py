#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create and return a new matrix where each element is squared
    return [[x**2 for x in row] for row in matrix]

