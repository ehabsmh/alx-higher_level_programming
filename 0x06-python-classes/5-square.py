#!/usr/bin/python3

""" Define a class Square """


class Square:

    """ Initialize a new square

    Args:
        __size: The size of the new square.
    """
    def __init__(self, __size=0):

        self.__size = __size

    """ Public instance method that returns the current square area """
    def area(self):

        return self.__size ** 2

    """ Property to get the size of the square """
    @property
    def size(self):
        """ size - returns __size of the square """

        return self.__size

    """ Setter property to update the private `__size` """
    @size.setter
    def size(self, value):
        """ size - sets a value to __size """

        self.__size = value
        """ __size must be an integer """
        if not isinstance(self.__size, int):

            raise TypeError("size must be an integer")

        """ __size cannot be less than 0 """
        if self.__size < 0:

            raise ValueError("size must be >= 0")

        """ my_print - prints the square with the character # """
    def my_print(self):

        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end='')
            print()
