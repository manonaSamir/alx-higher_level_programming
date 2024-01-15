#!/usr/bin/python3
"""rectangle.py"""
from models.base import Base


class Rectangle(Base):
    """Simple rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the private width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the private x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the private x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the private y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the private y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        line = " " * self.__x + "#" * self.__width + '\n'
        print(line * self.__height, end="")

    def __str__(self):
        """overriding the __str__ method so that it returns [Rectangle]"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:"""
        if args:
            allowed_keys = {'width', 'height', 'x', 'y'}
            for key, value in kwargs.items():
                if key in allowed_keys:
                    setattr(self, key, value)
        if kwargs:
            allowed_keys = {'id', 'width', 'height', 'x', 'y'}
            for key, value in kwargs.items():
                if key in allowed_keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
