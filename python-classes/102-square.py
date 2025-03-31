#!/usr/bin/python3
"""
This module defines a class Square with properties for size and methods
for comparing square instances based on their area.
"""

class Square:
    """
    A class that defines a square by its size.
    
    Attributes:
        size (int or float): The size of the square (length of one side).
    """

    def __init__(self, size=0):
        """
        Initializes a new square with a given size.
        
        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If the value is not a number (int or float).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if the area of the square is equal to another square's area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the area of the square is not equal to another square's area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of the square is smaller than another square's area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if this square's area is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the square is less than or equal to another square's area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if this square's area is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of the square is greater than another square's area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if this square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the square is greater than or equal to another square's area.

        Args:
            other (Square): Another square to compare.

        Returns:
            bool: True if this square's area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()


