#!/usr/bin/python3
"""Define a class called Square"""


class Square:
  
    """Constructor method for initializing a Square object"""
    def __init__(self, size=0):
        """Set the 'size' attribute to the provided 'size' parameter
        (default to 0)"""
        self.size = size

    """Getter method for 'size' attribute, used as a property"""
    @property
    def size(self):
        """Return the private attribute '__size'"""
        return (self.__size)

    """Setter method for 'size' attribute, used as a property"""
    @size.setter
    def size(self, value):
        """Check if the provided 'value' is not an 
        integer, raise a TypeError"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        """Check if the provided 'value' is negative, raise a ValueError"""
        elif value < 0:
            raise ValueError("size must be >= 0")
        """Set the private attribute '__size' to the provided 'value'"""
        self.__size = value

    """Method to calculate the area of the square"""
    def area(self):
        """Return the area, which is the square of the '__size' attribute"""
        return (self.__size * self.__size)
