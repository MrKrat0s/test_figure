class Rectangle:

    def __new__(cls, side1, side2):
        if (side1 == 0) or (side2 == 0):
            raise ValueError
        if type(side1) != (int or float) or type(side2) != (int or float):
            raise TypeError
        return super().__new__(cls)

    def __init__(self, side1, side2):
        self.name = "Rectangle"
        self.__side1 = side1
        self.__side2 = side2
        self.perimeter = self.__calc_perimeter()
        self.area = self.__calc_area()

    def __calc_perimeter(self):
        return self.__side1 * 2 + self.__side2 * 2

    def __calc_area(self):
        return self.__side1 * self.__side2

    def add_area(self, obj):
        return self.area + obj.area
