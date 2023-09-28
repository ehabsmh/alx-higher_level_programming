#!/usr/bin/python3

""" Define a class Square """


class Square:

    """ Initialize a new square

    Args:
        size: The size of the new square.
    """
    def __init__(self, __size=0):

        self.__size = __size

    """ Public instance method that returns the current square area """
    def area(self):

        return self.__size ** 2

    """ Property to get the size of the square """
    @property
    def size(self):
        """ size - returns the size of the square """

        return self.__size

    """ Setter property to update the private `size` """
    @size.setter
    def size(self, value):
        """ size - sets a value to the size """

        self.__size = value
        """ size must be an integer """
        if not isinstance(self.__size, int):

            raise TypeError("size must be an integer")

        """ size cannot be less than 0 """
        if self.__size < 0:

            raise ValueError("size must be >= 0")
