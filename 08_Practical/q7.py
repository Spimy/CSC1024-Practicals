from utils import input_num
from math import sqrt, pi


def question_7():
    print('Enter centre point of a circle')
    centre = [int(input_num('x: ')), int(input_num('y: '))]

    print('Enter a point on the circle')
    point = [int(input_num('x: ')), int(input_num('y: '))]

    r = radius(centre[0], centre[1], point[0], point[1])
    c = circumference(r)
    a = area(r)

    print('Radius', r)
    print('Circumference', c)
    print('Area', a)


def distance():
    # Not sure what this is asking? Isn't this the same as radius?
    pass


def radius(centre_x, centre_y, point_x, point_y):
    return sqrt((centre_x-point_x)**2 + (centre_y-point_y)**2)


def circumference(radius):
    return 2 * pi * radius


def area(radius):
    return pi * radius ** 2
