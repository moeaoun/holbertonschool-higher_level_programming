#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""

class Square:
    """
    A class representing a square.
    The square has a private instance attribute `size` that represents its side length.
    """
    def __init__(self, size):
        """
        Initialize a new square with the given size.
        
        Args:
            size (int): The length of the side of the square.
        """
        self.__size = size

