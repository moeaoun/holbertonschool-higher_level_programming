#!/usr/bin/python3
"""
This module defines a class Square with properties for size and position,
along with methods for printing and calculating the area of the square.
"""

class Square:
    """
    A class that defines a square by its size and position.
    
    Attributes:
        size (int): The size of the square (length of one side).
        position (tuple): A tuple representing the position of the square
                          in a 2D grid (row, column).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with a given size and position.
        
        Args:
            size (int): The size of the square.
            position (tuple): A tuple of two positive integers indicating the 
                              position of the square on a grid.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive integers indicating the position.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
           not all(isinstance(i, int) for i in value) or
           not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' using the current position
        (number of spaces to move to the right and down).
        If the size is 0, it prints an empty line.
        """
        if self.size == 0:
            print()
            return

        # Print rows of the square with correct positioning
        for i in range(self.position[1]):
            print()  # Print empty lines for vertical position

        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.

        This uses the same logic as my_print() but instead of printing directly,
        it returns the string.
        """
        if self.size == 0:
            return ""

        # Collect the square string with the correct position and size
        result = []
        for i in range(self.position[1]):
            result.append("")  # Add empty lines for vertical position

        for i in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(result)

