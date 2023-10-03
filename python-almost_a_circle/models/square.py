#!/usr/bin/python3
"""
The class Square that inherits from Rectangle.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square: a subclass of Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Getter for the size property.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size property.

        Args:
            value (int): The new size of the square.
        """
        self.height = value
        self.width = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format "[Square] (id) x/y - size".
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes using positional and keyword arguments.

        Args:
            *args: Positional arguments representing the attributes to update.
            **kwargs: Keyword arguments representing the attributes to update.
        """
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
