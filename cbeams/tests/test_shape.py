from math import sqrt

import pytest

from .. import shape
from ..shape import Strip

EPSILON = 0.01

def test_subtract_row_no_subtracts():
    assert shape._subtract_row([Strip(0, 1, 5)], []) == [Strip(0, 1, 5)]

def test_subtract_row_cut_in_two():
    # shape  12345
    #  hole   23
    # result 1  45
    assert \
        shape._subtract_row([Strip(0, 1, 5)], [Strip(0, 2, 2)]) == \
        [Strip(0, 1, 1), Strip(0, 4, 2)]

def test_disc_radius_lt_0_should_raise():
    with pytest.raises(ValueError):
        shape.disc(1, 1, -EPSILON)

def test_disc_radius_0():
    # r==0 is a special case, blank
    assert shape.disc(3, 3, 0) == []

def test_disc_radius_lt_1():
    # 0 <  r < 1:                #
    # (Irregular compared to all the cases below, in that the first '<'
    # is not a '<=', due to the special case of r==0)
    EXPECTED = [
        (3, 3, 1)  #
    ]
    assert shape.disc(3, 3, 0 + EPSILON) == EXPECTED
    assert shape.disc(3, 3, 1 - EPSILON) == EXPECTED

def test_disc_radius_1():
    # 1 <= r < sqrt(2)
    EXPECTED = [
        (2, 3, 1),  #
        (3, 2, 3), ###
        (4, 3, 1),  #
    ]
    assert shape.disc(3, 3, 1) == EXPECTED
    assert shape.disc(3, 3, sqrt(2) - EPSILON) == EXPECTED

def test_disc_radius_sqrt_2():
    # sqrt(2) <= r < 2
    EXPECTED = [
        (2, 2, 3), ###
        (3, 2, 3), ###
        (4, 2, 3), ###
    ]
    assert shape.disc(3, 3, sqrt(2)) == EXPECTED
    assert shape.disc(3, 3, 2 - EPSILON) == EXPECTED

def test_disc_radius_2():
    # 2 <= r < sqrt(5)
    EXPECTED = [
        (1, 3, 1),   #
        (2, 2, 3),  ###
        (3, 1, 5), #####
        (4, 2, 3),  ###
        (5, 3, 1),   #
    ]
    assert shape.disc(3, 3, 2) == EXPECTED
    assert shape.disc(3, 3, sqrt(5) - EPSILON) == EXPECTED

def test_disc_radius_sqrt_5():
    # sqrt(5) <= r < sqrt(8)
    EXPECTED = [
        Strip(*s) for s in [
            (1, 2, 3),  ###
            (2, 1, 5), #####
            (3, 1, 5), #####
            (4, 1, 5), #####
            (5, 2, 3),  ###
        ]
    ]
    assert shape.disc(3, 3, sqrt(5)) == EXPECTED
    assert shape.disc(3, 3, sqrt(8) - EPSILON) == EXPECTED

def test_annulus_radius_2_1():
    EXPECTED = [
        Strip(*s) for s in [
            (1, 3, 1),              #
            (2, 2, 1), (2, 4, 1),  # #
            (3, 1, 1), (3, 5, 1), #   #
            (4, 2, 1), (4, 4, 1),  # #
            (5, 3, 1),              #
        ]
    ]
    assert list(shape.annulus(3, 3, 2, 1)) == EXPECTED

