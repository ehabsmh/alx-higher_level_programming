#!/usr/bin/python3

""" Define a class Square """


class Square:

    """ Initialize a new square

    Args:
        size: The size of the new square.
    """
    def __init__(self, __size=0):

        self.__size = __size

        """ size must be an integer """
        if not isinstance(__size, int):

            raise TypeError("size must be an integer")

        """ size cannot be less than 0 """
        if __size < 0:

            raise ValueError("size must be >= 0")

    """ Public instance method that returns the current square area """
    def area(self):

        return self.__size ** 2
