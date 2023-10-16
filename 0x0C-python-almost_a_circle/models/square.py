#!/usr/bin/python3

"""Defines square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines size, x, y and id"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes objects of type Square"""

        super().__init__(size, size, x, y, id)

    # ___________________________________________________________________

    def __str__(self):
        """Square instance string representation"""
        dimensions = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {dimensions} - {self.width}"

    # ___________________________________________________________________

    @property
    def size(self):
        """Return: width"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the width with a specific value and assign it to the height"""

        self.width = value
        self.height = self.width

    # ___________________________________________________________________

    def update(self, *args, **kwargs):
        """
        This method updates the attributes with args and kwargs

        Args:
            args: is variable args of non key-value pairs
            kwargs: is variable args of key-value pairs
        """

        arg_keys = ("id", "size", "x", "y")

        for i, arg in enumerate(args[:len(arg_keys)]):
            setattr(self, arg_keys[i], arg)

        if args and len(args) > 0:
            return

        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    # ___________________________________________________________________

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        my_dict = {}

        my_list = ("id", "size", "x", "y")

        for ele in my_list:
            rect_attribute = getattr(self, ele)
            my_dict[ele] = rect_attribute

        return my_dict
