from triangle import Triangle
from rectangle import Rectangle


t1 = Triangle(2, 4, 5)
t2 = Triangle(3, 7, 7)

r1 = Rectangle(2, 3)
r2 = Rectangle(1, 10)


print("Name : {}, Perimeter : {}, Area: {}".format(t1.name, t1.perimeter, t1.area))
print("Name : {}, Perimeter : {}, Area: {}".format(t2.name, t2.perimeter, t2.area))
print("Name : {}, Perimeter : {}, Area: {}".format(r1.name, r1.perimeter, r1.area))
print("Name : {}, Perimeter : {}, Area: {}".format(r2.name, r2.perimeter, r2.area))

print("Area 1 : {}, Area 2 : {}, sum area : {}".format(t1.area, t2.area, t1.add_area(t2)))
print("Area 1 : {}, Area 2 : {}, sum area : {}".format(r1.area, r2.area, r1.add_area(r2)))
print("Area 1 : {}, Area 2 : {}, sum area : {}".format(r1.area, t2.area, r1.add_area(t2)))
print("Area 1 : {}, Area 2 : {}, sum area : {}".format(t1.area, r2.area, t1.add_area(r2)))

