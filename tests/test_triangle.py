from triangle import Triangle
from rectangle import Rectangle
import testtools as tt
import pytest


class TestTriangle:
    """Tests create object"""

    @pytest.mark.parametrize("side1, side2, side3", tt.create_some_triangle(3))
    def test_create_triangle(self, side1, side2, side3):
        assert Triangle(side1, side2, side3) is not None

    @pytest.mark.parametrize("side1, side2, side3", [(0, 1, 1),
                                                     (1, 0, 1),
                                                     (1, 1, 0),
                                                     (2, 2, 4)])
    def test_create_wrong_triangle(self, side1, side2, side3):
        assert Triangle(side1, side2, side3) is None

    @pytest.mark.parametrize("side1, side2, side3", tt.create_some_triangle(3))
    def test_check_name(self, side1, side2, side3):
        assert Triangle(side1, side2, side3).name == "Triangle"

    """Tests object calc parameters"""

    @pytest.mark.parametrize("side1, side2, side3, raise_error", [("1", 1, 1, TypeError),
                                                                  (1, True, 1, TypeError),
                                                                  (1, 1, [1, 0], TypeError)]) #and etc.
    def test_wrong_types(self, side1, side2, side3, raise_error):
        with pytest.raises(raise_error):
            Triangle(side1, side2, side3)

    @pytest.mark.parametrize("side1, side2, side3", tt.create_some_triangle(3))
    def test_check_calc_perimeter(self, side1, side2, side3):
        assert Triangle(side1, side2, side3).perimeter == tt.calc_perimeter_triangle(side1, side2, side3)
        return

    @pytest.mark.parametrize("side1, side2, side3", tt.create_some_triangle(3))
    def test_check_calc_area(self, side1, side2, side3):
        assert Triangle(side1, side2, side3).area == tt.calc_area_triangle(side1, side2, side3)

    """Tests object methods"""
    @pytest.mark.parametrize("sides1, sides2", [(tt.random_sides_triangle(), tt.random_sides_triangle())])
    def test_check_def_add_area_same_object(self, sides1, sides2):
        assert Triangle(sides1[0], sides1[1], sides1[2]).add_area(Triangle(sides2[0], sides2[1], sides2[2])) == \
               tt.calc_area_triangle(sides1[0], sides1[1], sides1[2]) + tt.calc_area_triangle(sides2[0], sides2[1], sides2[2])

    @pytest.mark.parametrize("sides_triangle, sides_object", [(tt.random_sides_triangle(), tt.random_sides_rectangle())])
    def test_check_def_add_area_other_object(self, sides_triangle, sides_object):
        assert Triangle(sides_triangle[0], sides_triangle[1], sides_triangle[2]).add_area(Rectangle(sides_object[0],
                                                                                                    sides_object[1])) \
               == tt.calc_area_triangle(sides_triangle[0], sides_triangle[1], sides_triangle[2]) + \
               tt.calc_area_rectangle(sides_object[0],
                                                                                                    sides_object[1])
    
    @pytest.mark.parametrize("side1, side2, side3", tt.create_some_triangle())
    def test_check_def_add_area_wrong_object(self, side1, side2, side3):
        sides = tt.random_sides_triangle()
        with pytest.raises(AttributeError):
            Triangle(side1, side2, side3).add_area(object)


