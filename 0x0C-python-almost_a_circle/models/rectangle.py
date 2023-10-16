#!/usr/bin/python3

"""
Defines class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """defines rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes rectangle object

        Args:
            width: the width of a rectangle
            height: the height of a rectangle
            x:
            y:
            id: Identifier for object, inherited from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # _______________________________________________________

    @classmethod
    def __validate_attribute(cls, att_name, value):
        """
        This method validates the specified value

        Args:
            att_name: the attribute name
            value: the value of the width

        Exceptions:
            TypeError: value must be integer
            ValueError: value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{att_name} must be an integer")

        if att_name in ["width", "height"]:
            if value <= 0:
                raise ValueError(f"{att_name} must be > 0")

        if att_name in ["x", "y"]:
            if value < 0:
                raise ValueError(f"{att_name} must be >= 0")

    # _______________________________________________________

    @property
    def width(self):
        """
        This method gets the width value

        Return: width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method validates the value and sets the width
        with the specified value

        Args:
            value: the value of the width

        """
        Rectangle.__validate_attribute("width", value)
        self.__width = value

    # _______________________________________________________

    @property
    def height(self):
        """
        Gets the height value

        Return: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height to a specific value

        Args:
            @value: the value of the height

        Exceptions:
            TypeError: height must be integer
            ValueError: height must be greater than 0.
        """
        Rectangle.__validate_attribute("height", value)
        self.__height = value

    # _______________________________________________________

    @property
    def x(self):
        """
        Gets the x value

        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets x to a specific value

        Args:
            @value: the value of x

        Exceptions:
            TypeError: x must be integer
            ValueError: x must be greater than or equal to 0.
        """

        Rectangle.__validate_attribute("x", value)
        self.__x = value

    # _______________________________________________________

    @property
    def y(self):
        """
        This method gets y

        Return: y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This method sets y to a specific value

        Args:
            @value: the value of y

        Exceptions:
            TypeError: y must be an integer
            ValueError: y must be greater than or equal to 0.
        """
        Rectangle.__validate_attribute("y", value)
        self.__y = value

    # _______________________________________________________

    def area(self):
        """ area = width * height """
        return self.__width * self.__height

    # _______________________________________________________

    def display(self):
        """
        This method prints in stdout the Rectangle instance
        with the character #
        """
        print('\n' * self.__y, end='')

        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width + '\n', end='')

    # _______________________________________________________

    def __str__(self):
        dimensions = f"{self.__x}/{self.__y}"
        measurement = f"{self.__width}/{self.__height}"
        return f"{Rectangle.__name__} ({self.id}) {dimensions} - {measurement}"

    # _______________________________________________________

    def update(self, *args, **kwargs):

        arg_keys = ("id", "width", "height", "x", "y")

        for i, arg in enumerate(args[:len(arg_keys)]):
            setattr(self, arg_keys[i], arg)

        if args and len(args) > 0:
            return

        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
