#!/usr/bin/python3
"""
Generate Pascal's Triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    If n <= 0, return an empty list.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    triangle = [[1]]  # The first row of the triangle is always [1]

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        
        # Generate the inner elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the row to the triangle

    return triangle

