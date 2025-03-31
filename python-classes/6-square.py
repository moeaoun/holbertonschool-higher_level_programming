#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes.
It also includes methods to calculate the area and print the square
at the given position.
"""

class Square:
    """
    A class representing a square with a size and position.

    The size must be a non-negative integer.
    The position must be a tuple of two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square with a given size and position.

        Args:
            size (int): The length of the side of the square. Default is 0.
            position (tuple): A tuple of two integers representing the
                              position of the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 integers.
            ValueError: If size is less than 0 or position elements are less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: A tuple of two integers representing the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two integers.
            ValueError: If any element in the tuple is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout using the '#' character at the
        specified position.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            # Print the vertical space (position[1] number of empty lines)
            for _ in range(self.__position[1]):
                print("")
            # Print the square with leading spaces
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

