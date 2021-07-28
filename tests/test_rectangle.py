from rectangle import Rectangle
from triangle import Triangle
import testtools as tt
import pytest


class TestRectangle:
    """Tests create object"""

    @pytest.mark.parametrize("side1, side2", tt.create_some_rectangle(3))
    def test_create_rectangle(self, side1, side2):
        assert Rectangle(side1, side2) is not None

    @pytest.mark.parametrize("side1, side2, raise_error", [(1, 0, ValueError),
                                                           (0, 1, ValueError),
                                                           ("1", 1, TypeError),
                                                           (1, True, TypeError),
                                                           ([1, 0], 1, TypeError)])  # and etc.
    def test_create_wrong_rectangle(self, side1, side2, raise_error):
        with pytest.raises(raise_error):
            Rectangle(side1, side2)

    @pytest.mark.parametrize("side1, side2", tt.create_some_rectangle(3))
    def test_check_name(self, side1, side2):
        assert Rectangle(side1, side2).name == "Rectangle"

    """Tests object calc parameters"""

    @pytest.mark.parametrize("side1, side2", tt.create_some_rectangle(3))
    def test_check_calc_perimeter(self, side1, side2):
        assert Rectangle(side1, side2).perimeter == tt.calc_perimeter_rectangle(side1, side2)

    @pytest.mark.parametrize("side1, side2", tt.create_some_rectangle(3))
    def test_check_calc_area(self, side1, side2):
        assert Rectangle(side1, side2).area == tt.calc_area_rectangle(side1, side2)

    """Tests object methods"""

    @pytest.mark.parametrize("sides1, sides2", [(tt.random_sides_rectangle(), tt.random_sides_rectangle())])
    def test_check_def_add_area_same_object(self, sides1, sides2):
        assert Rectangle(sides1[0], sides1[1]).add_area(Rectangle(sides2[0], sides2[1])) == \
               tt.calc_area_rectangle(sides1[0], sides1[1]) + tt.calc_area_rectangle(sides2[0], sides2[1])

    @pytest.mark.parametrize("sides_rect, sides_object", [(tt.random_sides_rectangle(), tt.random_sides_triangle())])
    def test_check_def_add_area_other_object(self, sides_rect, sides_object):
        assert Rectangle(sides_rect[0], sides_rect[1]).add_area(Triangle(sides_object[0], sides_object[1],
                                                                         sides_object[2])) \
               == tt.calc_area_rectangle(sides_rect[0], sides_rect[1]) + tt.calc_area_triangle(sides_object[0],
                                                                                               sides_object[1],
                                                                                               sides_object[2])

    @pytest.mark.skip()
    @pytest.mark.parametrize("side1, side2", tt.create_some_rectangle())
    def test_check_def_add_area_wrong_object(self, side1, side2):
        sides = tt.random_sides_rectangle()
        with pytest.raises(AttributeError):
            Rectangle(side2, side1).add_area(object)
