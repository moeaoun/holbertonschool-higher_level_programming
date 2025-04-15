#!/usr/bin/python3
"""
This module defines a Student class with JSON serialization capabilities.
"""

class Student:
    """
    Defines a student by first name, last name, and age, and allows
    retrieval of JSON representations with an optional attribute filter.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance,
        with optional filtering of attributes.

        Args:
            attrs (list, optional): A list of attribute names to retrieve. 
                                     If None, all attributes are returned.

        Returns:
            dict: A dictionary representation of the student's attributes.
        """
        if attrs is None:
            return self.__dict__

        # Create a filtered dictionary with only the allowed attributes
        return {key: value for key, value in self.__dict__.items() if key in attrs}

