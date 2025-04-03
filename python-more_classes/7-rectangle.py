#!/usr/bin/python3
"""Rectangle class that defines a rectangle."""

class Rectangle:
    """Defines a rectangle by width and height with validation."""

    number_of_instances = 0  # Class attribute to keep track of instances
    print_symbol = "#"  # Class attribute to control the symbol used for string representation

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment class attribute on creation

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle with print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle that can be used to recreate the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when the rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement class attribute on deletion

