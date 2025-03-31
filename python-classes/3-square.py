#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""

class Square:
    """
    A class representing a square with a size attribute.
    
    The size of the square must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initialize a square with a given size.
        
        Args:
            size (int): The length of the side of the square. Default is 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

