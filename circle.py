import math


def area(r):
    '''Принимает r - радиус круга, возвращает его площадь'''
    if r < 1:
        raise ValueError('radius cannot be less than 0')
    return math.pi * r * r


def perimeter(r):
    '''Принимает r - радиус круга, возвращает его периметр'''
    if r < 0:
        raise ValueError('radius cannot be less than 0')
    return 2 * math.pi * r
