#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
    def __init__(self, size=0):
        """The init method initializes the size of the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
