#!/usr/bin/python3
""" Square subclass
    that inherits from
    Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ subclass of Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiate attributes of square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ setter for width and height of square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def __str__(self):
        """ print instance of a Square class """
        s = '[' + (str(self.__class__.__name__)) + ']' + ' '
        s += '(' + (str(self.id)) + ')' + ' '
        s += str(self.x) + '/' + str(self.y) + ' - '
        s += str(self.width)
        return s

    def update(self, *args, **kwargs):
        """ update attributes using *args """
        """ we can also use this one
        if args and len(args) > 0:

            try:
                if args[0] is not None:
                    self.id = args[0]
                else:
                    super.__init__(self.width, self.height, self.x, self.y)
                if args[1]:
                    self.width = args[1]
                if args[2]:
                    self.height = args[2]
                if args[3]:
                    self.x = args[3]
                if args[4]:
                    self.__y = args[4]
            except:
                pass
            """
        if args and len(args) > 0: # TODO: task 8. Update #0

            for count, arg in enumerate(args):
                if count == 0:
                    if arg is None:
                        self.__init__(self.width,
                                         self.height,
                                         self.x, self.y)
                    else:
                        self.id = args[count]
                if count == 1:
                    self.width = args[count]
                    self.height = args[count]
                if count == 2:
                    self.x = args[count]
                if count == 3:
                    self.y = args[count]
        elif kwargs and len(kwargs) > 0:    #TODO: 9. Update #1
            """ loop accros the dictionary """
            for key in kwargs:
                if key == "id":
                    if kwargs[key] is None:
                        self.__init__(self.width,
                                       self.height,
                                       self.x, self.y)
                    else:
                        self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ return dictionary of attributes """
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}