import math


class Triangle:

    def __new__(cls, side1, side2, side3):
        if type(side1) != (int or float) or type(side2) != (int or float) or type(side3) != (int or float):
            raise TypeError
        if not cls.__check_triangle(side1, side2, side3):
            # print("Error: this triangle cannot exist")
            return None
        return super().__new__(cls)

    def __init__(self, side1, side2, side3):
        self.name = "Triangle"
        self.__side1 = int(side1)
        self.__side2 = int(side2)
        self.__side3 = int(side3)
        self.perimeter = self.__calc_perimeter()
        self.area = self.__calc_area()

    @classmethod
    def __check_triangle(cls, side1, side2, side3):
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            return False
        return True

    def __calc_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __calc_area(self):
        half_perimeter = self.perimeter / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.__side1) * (half_perimeter - self.__side2) * (half_perimeter - self.__side3))

    def add_area(self, obj):
        return self.area + obj.area


