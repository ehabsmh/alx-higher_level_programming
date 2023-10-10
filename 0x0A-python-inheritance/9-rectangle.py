#!/usr/bin/python3

"""This module contains a class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define Rectangle class"""

    def __init__(self, width, height):
        """Initializes object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of a rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
