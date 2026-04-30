#!/usr/bin/python3
"""define a class called Square"""


class Square:
    """Defines a square with a private size"""

    def __init__(self, size):
        """
        Initializes a new square instance.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
