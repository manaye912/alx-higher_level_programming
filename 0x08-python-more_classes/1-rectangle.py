#!/usr/bin/python3
"""
A rectangle with width and height.
"""
class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Instantializing the rectangle by 
        setting the object wih width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the priate instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"
        Setter methode
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
