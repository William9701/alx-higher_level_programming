#!/usr/bin/python3
"""Defines a square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ this a square class which inherits a rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ returns width as size """

        return self.width

    @size.setter
    def size(self, value):
        """ this chks the size and sets it to the value of width and height """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """ prints string represantaion of the square """

        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @classmethod
    def create(cls, **dictionary):
        """ creates a dict rep of the list """

        dummy_rect = cls(dictionary.get('size', 0), dictionary.get('x', 0),
                         dictionary.get('y', 0), dictionary.get('id', 0))
        dummy_rect.update(**dictionary)
        return dummy_rect

    def update(self, *args, **kwargs):
        """ updates the code """

        if args and len(args) != 0:
            if args is None:
                self.__init__(self.size, self.x, self.y)
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            if kwargs is None:
                self.__init__(self.size, self.x, self.y)
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """ return a dict representaion of the list """

        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
