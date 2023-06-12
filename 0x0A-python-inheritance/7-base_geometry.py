#!/usr/bin/python3
"""
    7-base_geometry: class BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry
        Methods:
            area() - raises an Exception
            integer_validator() - validates value.
    """
    def area(self):
        """
            Area raise an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator checks the value of value.
            Arguments:
                name (str): name
                value (int): value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
