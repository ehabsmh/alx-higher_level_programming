#!/usr/bin/python3

""" This module contains a class `BaseGeometry` """


class BaseGeometry:
    """define class BaseGeometry"""

    def area(self):
        """raises an Exception"""

        raise Exception("area() is not implemented")

    # ____________________________________________________

    def integer_validator(self, name, value):
        """
        This function validating the value as integer

        Args:
          name: The name that holds the value
          value: The integer value

        Exceptions:
          TypeError: if value is not an integer
          ValueError: if value is less or equal to 0.
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initializes object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
