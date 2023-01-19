#!/usr/bin/python3
"""Define a class Square."""


class Square:
    '''Represent a square.'''

    def __init__(self, size=0):
        self.size = size
        '''Initialize a new square.

        Args:
            size (int): The size of the new square.
        '''

    @property
    def size(self):
        '''Get/set the current size of the square.'''

        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        if self._size == 0:
            print()
        else:
            print('\n'.join([''.join(['#' for _ in range(
                self._size)]) for _ in range(self._size)]))
