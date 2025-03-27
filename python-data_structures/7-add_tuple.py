#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Make sure tuple_a and tuple_b have at least 2 elements (pad with 0 if needed)
    a1, a2 = (tuple_a + (0, 0))[:2]  # Padding tuple_a if it has less than 2 elements
    b1, b2 = (tuple_b + (0, 0))[:2]  # Padding tuple_b if it has less than 2 elements

    # Return a tuple with the sum of corresponding elements
    return (a1 + b1, a2 + b2)

