#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute and getter and setter methods.
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
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.
        
        Returns:
            int: The length of the side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.
        
        Args:
            value (int): The length of the side of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

