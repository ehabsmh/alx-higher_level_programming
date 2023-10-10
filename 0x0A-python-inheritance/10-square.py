#!/usr/bin/python3

"""This module contains a class Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Define Square class"""

    def __init__(self, size):
        """Initializes object"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a Square."""
        return self.__size ** 2

    def __str__(self):
        """String representation of a Square."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
