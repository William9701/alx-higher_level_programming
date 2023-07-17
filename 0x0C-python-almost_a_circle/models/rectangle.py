#!/usr/bin/python3
"""Defines a rectangle class."""


from models.base import Base


class Rectangle(Base):
    """ a class rectangle that inherits from the class base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes the valuse of the code """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """ defines height as a private instance """

        return self.__height

    @height.setter
    def height(self, value):
        """ sets the valuse of the hieght """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def width(self):
        """ defines the width to a private instance """

        return self.__width

    @width.setter
    def width(self, value):
        """  sets the width to its valuse and also chks for abnorms """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """ defimses x ans a private instance """

        return self.__x

    @x.setter
    def x(self, value):
        """ sets x to its value and also chks for abnorms """

        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ defines y as a private instance """

        return self.__y

    @y.setter
    def y(self, value):
        """ sets y to its value and also chks for abnorms """

        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ return the are of the shape sent """

        return self.width * self.height

    def display(self):
        """ prints a representaion of the shape """

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(' ', end='')
            for _ in range(self.width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """ updates the value of the arguments """

        if args and len(args) != 0:
            if (args is None):
                self.__init__(self.width, self.height, self.x, self.y)
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            if (kwargs is None):
                self.__init__(self.width, self.height, self.x, self.y)
            for key, value in kwargs.items():
                if key == "height":
                    self.height = value
                if key == "width":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    @classmethod
    def create(cls, **dictionary):
        """ creats a dummy instace of the attribtes """

        dummy_rect = cls(dictionary.get('width', 0),
                dictionary.get('height', 0), dictionary.get('x', 0),
                dictionary.get('y', 0), dictionary.get('id', 0))
        dummy_rect.update(**dictionary)
        return dummy_rect

    def to_dictionary(self):
        """ returns a dict rep of the list passed """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ prints a srting rep of the code """

        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'
