from math import sqrt

import pytest

from ..shape import Shape

# If testing the x<y case, we use x = y - EPSILON
EPSILON = 0.01

def test_constructor():
    shape = Shape('strips')
    assert shape.strips == 'strips'


def test_rectfill():
    assert Shape.RectFill(0, 1, 2, 4).strips == [
        (0, 1, 4),
        (1, 1, 4),
        (2, 1, 4),
    ]

def test_rectfill_should_handle_minimal_case():
    assert Shape.RectFill(1, 1, 1, 1).strips == [ (1, 1, 1) ]

def test_rectfill_with_unordered_args_should_raise():
    with pytest.raises(ValueError):
        Shape.RectFill(1, 1, 0, 1)
    with pytest.raises(ValueError):
        Shape.RectFill(1, 1, 1, 0)

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

def test_clipped_left():
    shape = Shape([
        (1, 0, 10), # not clipped
        (2, -2, 6), # clipped to length 4
        (3, -4, 5), # clipped to length 1
        (4, -6, 6), # clipped to length 0, i.e. removed entirely
    ])
    assert list(shape.clipped(99, 10)) == [
        (1, 0, 10),
        (2, 0, 4),
        (3, 0, 1),
    ]

def test_clipped_right():
    shape = Shape([
        (1, 0, 10), # not clipped
        (2, 0, 11), # clipped to length 10
        (3, 9, 99), # clipped to length 1
        (4, 10, 99), # clipped to length 0, i.e. removed entirely
    ])
    assert list(shape.clipped(99, 10)) == [
        (1, 0, 10),
        (2, 0, 10),
        (3, 9, 1),
    ]

def test_clipped_top_and_bottom():
    shape = Shape([
        (-1, 0, 10), # removed entirely
        (0, 0, 10), # not clipped
        (9, 0, 10), # not clipped
        (10, 0, 10), # removed entirely
    ])
    assert list(shape.clipped(10, 99)) == [
        (0, 0, 10),
        (9, 0, 10),
    ]

