import random
import math
__MAX_SIDE = 100


def random_sides_triangle():
    sides = []
    sides.append(random.randrange(1, __MAX_SIDE // 2))
    sides.append(random.randrange(sides[0], __MAX_SIDE))
    sides.append(random.randrange(max(sides[0], sides[1]), sides[0] + sides[1]))
    # print("{} : {} : {}".format(list[0], list[1], list[2]))
    return sides


def create_some_triangle(count=1):
    triangle = []
    for i in range(count):
        triangle.append(random_sides_triangle())
    return triangle


def random_sides_rectangle():
    sides = [random.randrange(1, __MAX_SIDE), random.randrange(1, __MAX_SIDE)]
    # print("{} : {}".format(list[0], list[1]))
    return sides


def create_some_rectangle(count=1):
    rectangle = []
    for i in range(count):
        rectangle.append(random_sides_rectangle())
    return rectangle


def calc_perimeter_triangle(side1, side2, side3):
    return side1+ side2 + side3


def calc_perimeter_rectangle(side1, side2):
    return side1 * 2 + side2 * 2


def calc_area_triangle(side1, side2, side3):
    half_perimeter = calc_perimeter_triangle(side1, side2, side3) / 2
    return math.sqrt(half_perimeter * (half_perimeter - side1) * (half_perimeter - side2)
                     * (half_perimeter - side3))


def calc_area_rectangle(side1, side2):
    return side1 * side2
