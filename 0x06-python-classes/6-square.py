#!/usr/bin/python3

""" Define a class Square """


class Square:

    """ Initialize a new square

    Args:
        size: The size of the new square.
        position: The position of the new square.
    """
    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    """ size - Getter Property to get the size of the square """
    @property
    def size(self):
        """ size - returns __size of the square """
        return self.__size

    """ size - Setter property to update the private `__size` """
    @size.setter
    def size(self, value):

        """ __size must be an integer """
        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        """ __size cannot be less than 0 """
        if value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value

    """ position - Getter Property to get the __position of a square """
    @property
    def position(self):
        return self.__position

    """ position - Setter property to update the private __position """
    @position.setter
    def position(self, value):

        """ __position must be a tuple of 2 positive integers """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    """ area - Public instance method that returns the current square area """
    def area(self):

        return self.__size ** 2

        """ my_print - prints the square with the character # """
    def my_print(self):

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):

            for _ in range(self.__position[0]):

                print(" ", end='')

            for _ in range(self.__size):

                print("#", end='')

            print()
