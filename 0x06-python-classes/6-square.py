#!/usr/bin/python3
"""This moduke contains a class 'Square'"""


class Square:
    """This class represemts a 'Square'"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for 'size'"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for 'property'"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for 'position'"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current square area"""
        curr_sq_area = self.__size * self.__size
        return curr_sq_area

    def my_print(self):
        """Prints the square using the '#' character"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
