#!/usr/bin/python3
"""This is a locked module """


class LockedClass:
    """ This s a locked class """

    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if hasattr(self, name) or name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object\
                    has no attribute '{}'".format(name))
