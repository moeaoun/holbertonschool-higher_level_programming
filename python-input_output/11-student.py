#!/usr/bin/python3
"""
This module defines a Student class with methods for serialization and deserialization.
"""

class Student:
    """
    Defines a student by first name, last name, and age, with methods
    to serialize (to_json) and deserialize (reload_from_json) the object.
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

    def reload_from_json(self, json):
        """
        Reloads the student attributes from a dictionary (JSON representation).

        Args:
            json (dict): A dictionary representing a student with keys as attribute names
                         and values as the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)

