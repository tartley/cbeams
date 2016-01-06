from math import sqrt

import pytest

from .. import shape
from ..shape import Shape

# If testing the x<y case, we use x = y - EPSILON
EPSILON = 0.01

def test_constructor():
    shape = Shape('strips')
    assert shape.strips == 'strips'


def test_rect():
    assert shape.rect(0, 1, 2, 4).strips == [
        (0, 1, 4),
        (1, 1, 4),
        (2, 1, 4),
    ]

def test_rect_should_handle_minimal_case():
    assert shape.rect(1, 1, 1, 1).strips == [ (1, 1, 1) ]

def test_rect_with_unordered_args_should_raise():
    with pytest.raises(ValueError):
        shape.rect(1, 1, 0, 1)
    with pytest.raises(ValueError):
        shape.rect(1, 1, 1, 0)

def test_circlefill_radius_lt_0_should_raise():
    with pytest.raises(ValueError):
        Shape.CircleFill(1, 1, -EPSILON)

def test_circlefill_radius_0():
    # r==0 is a special case, blank
    assert Shape.CircleFill(3, 3, 0).strips == []

def test_circlefill_radius_lt_1():
    # 0 <  r < 1:                #
    # (Irregular compared to all the cases below, in that the first '<'
    # is not a '<=', due to the special case of r==0)
    EXPECTED = [
        (3, 3, 1)  #
    ]
    assert Shape.CircleFill(3, 3, 0 + EPSILON).strips == EXPECTED
    assert Shape.CircleFill(3, 3, 1 - EPSILON).strips == EXPECTED

def test_circlefill_radius_1():
    # 1 <= r < sqrt(2)
    EXPECTED = [
        (2, 3, 1),  #
        (3, 2, 3), ###
        (4, 3, 1),  #
    ]
    assert Shape.CircleFill(3, 3, 1).strips == EXPECTED
    assert Shape.CircleFill(3, 3, sqrt(2) - EPSILON).strips == EXPECTED

def test_circlefill_radius_sqrt_2():
    # sqrt(2) <= r < 2
    EXPECTED = [
        (2, 2, 3), ###
        (3, 2, 3), ###
        (4, 2, 3), ###
    ]
    assert Shape.CircleFill(3, 3, sqrt(2)).strips == EXPECTED
    assert Shape.CircleFill(3, 3, 2 - EPSILON).strips == EXPECTED

def test_circlefill_radius_2():
    # 2 <= r < sqrt(5)
    EXPECTED = [
        (1, 3, 1),   #
        (2, 2, 3),  ###
        (3, 1, 5), #####
        (4, 2, 3),  ###
        (5, 3, 1),   #
    ]
    assert Shape.CircleFill(3, 3, 2).strips == EXPECTED
    assert Shape.CircleFill(3, 3, sqrt(5) - EPSILON).strips == EXPECTED

def test_circlefill_radius_sqrt_5():
    # sqrt(5) <= r < sqrt(8)
    EXPECTED = [
        (1, 2, 3),  ###
        (2, 1, 5), #####
        (3, 1, 5), #####
        (4, 1, 5), #####
        (5, 2, 3),  ###
    ]
    assert Shape.CircleFill(3, 3, sqrt(5)).strips == EXPECTED
    assert Shape.CircleFill(3, 3, sqrt(8) - EPSILON).strips == EXPECTED

