
def area(a):
    '''Принимает a - длину стороны квадрата, возвращает его площадь'''
    if a < 0:
        raise ValueError('a cannot be less than 0')
    return a * a


def perimeter(a):
    '''Принимает a - длину стороны квадрата, возвращает его периметр'''
    if a < 0:
        raise ValueError('a cannot be less than 0')
    return 4 * a
