#!/usr/bin/python3
""" Description goes here """
Base = __import__('base').Base


class Rectangle(Base):
    """ Description for function goes here """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a rectangle
            Args:

            Raises:
                TypeError:
                ValueError:
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ Setter for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ Calculates area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Display the Rectangle """
        for y in range(self.__y):
            print('|')
        for height in range(self.__height):

            for x in range(self.__x):
                print('-', end='')
            for width in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ print instance of a class """
        s = '[' + (str(self.__class__.__name__)) + ']' + ' '
        s += '(' + (str(self.id)) + ')' + ' '
        s += str(self.__x) + '/' + str(self.__y) + ' - '
        s += str(self.__width) + '/' + str(self.__height)
        return s

    def update(self, *args):    # TODO: task 8. Update #0
        """ update attributes using *args """

        if args and len(args) > 0:
            """ we can also use this one
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
        if args and len(args) > 0:

            for count, arg in enumerate(args):
                if count == 0:
                    if arg is None:
                        super().__init__(self.width,
                                         self.height,
                                         self.x, self.y)
                    else:
                        self.id = args[count]
                if count == 1:
                    self.width = args[count]
                if count == 2:
                    self.height = args[count]
                if count == 3:
                    self.x = args[count]
                if count == 4:
                    self.y = args[count]
