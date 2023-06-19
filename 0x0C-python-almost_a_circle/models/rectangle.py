#!/usr/bin/python3
""" Description goes here """
from models.base import Base


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
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):     # TODO: 4. Area first
        """ Calculates area of the rectangle """
        return (self.__width * self.__height)

    #
    # def display(self):  # TODO: 5. Display #0
    #     """ Display the Rectangle """
    #     for y in range(self.__y):
    #         print(' ')
    #     for height in range(self.__height):

    #         for x in range(self.__x):
    #             print(' ', end='')
    #         for width in range(self.__width):
    #             print("#", end='')
    #         print()

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):  # TODO: 6. __str__
        """ print instance of a class """
        s = '[' + (str(self.__class__.__name__)) + ']' + ' '
        s += '(' + (str(self.id)) + ')' + ' '
        s += str(self.__x) + '/' + str(self.__y) + ' - '
        s += str(self.__width) + '/' + str(self.__height)
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
        if args and len(args) > 0:  # TODO: task 8. Update #0

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
                if count == 2:
                    self.height = args[count]
                if count == 3:
                    self.x = args[count]
                if count == 4:
                    self.y = args[count]
        elif kwargs and len(kwargs) > 0:    # TODO: 9. Update #1

            """ loop accros the dictionary """
            for key in kwargs:
                if key == "id":
                    if kwargs[key] is None:
                        self.__init__(self.width,
                                      self.height,
                                      self.x, self.y)
                    else:
                        self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
