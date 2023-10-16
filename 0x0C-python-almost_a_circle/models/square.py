#!/usr/bin/python3

"""Defines square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines size, x, y and id"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes objects of type Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square instance string representation"""
        dimensions = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {dimensions} - {self.width}"
