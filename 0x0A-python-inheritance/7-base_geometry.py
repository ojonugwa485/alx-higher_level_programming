#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Method to compute this area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
<<<<<<< HEAD
            raise ValueError("{} must be greater than 0".format(name)
=======
            raise ValueError("{} must be greater than 0".format(name))
>>>>>>> 0cbafcfe2ae56b3cb4d3fac5ab282431aee52175
