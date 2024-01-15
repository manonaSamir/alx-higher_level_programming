#!/usr/bin/python3
"""square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Simple Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square"""
        if args:
            i = 0
            allowed_keys = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, allowed_keys[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}

    def __str__(self):
        """gets rectangle"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.size)
