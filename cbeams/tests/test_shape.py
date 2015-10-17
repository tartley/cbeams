from math import sqrt
from unittest.mock import Mock, patch

import pytest

from ..shape import Shape

# If testing the x<y case, we use x = y - EPSILON
EPSILON = 0.01

def setup_function(_):
    Shape.terminal = get_mock_terminal()

def get_mock_terminal(**overrides):
    attrs = dict(
        move=lambda x, y: 'move({},{})'.format(x, y),
        height=11,
        width=22,
    )
    attrs.update(overrides)
    return Mock(**attrs)

def test_constructor():
    shape = Shape('strips')
    assert shape.strips == 'strips'

def test_str():
    shape = Shape([(1, 2, 3), (4, 5, 6)])
    assert str(shape) == 'move(1,2)' + ' ' * 3 + 'move(4,5)' + ' ' * 6


def test_rectfill():
    assert str(Shape.RectFill(0, 1, 2, 4)) == \
        'move(0,1)' + '    ' + \
        'move(1,1)' + '    ' + \
        'move(2,1)' + '    '

def test_rectfill_should_handle_minimal_case():
    assert str(Shape.RectFill(1, 1, 1, 1)) == 'move(1,1) '

def test_rectfill_with_unordered_args_should_raise():
    with pytest.raises(ValueError):
        Shape.RectFill(1, 1, 0, 1)
    with pytest.raises(ValueError):
        Shape.RectFill(1, 1, 1, 0)

def test_circlefill_radius_lt_0_should_raise():
    with pytest.raises(ValueError):
        Shape.CircleFill(1, 1, -EPSILON)

def test_circlefill_radius_0():
    # r==0 is a special case
    assert str(Shape.CircleFill(3, 3, 0)) == ''

def test_circlefill_radius_lt_1():
    #
    # 0 <  r < 1:                #
    #
    # (Irregular compared to all the cases below, in that the first '<'
    # is not a '<=', due to the special case of r==0)
    assert str(Shape.CircleFill(3, 3, 0 + EPSILON)) == 'move(3,3)' + ' '
    assert str(Shape.CircleFill(3, 3, 1 - EPSILON)) == 'move(3,3)' + ' '

def test_circlefill_radius_1():
    #                            #
    # 1 <= r < sqrt(2):         ###
    #                            #
    EXPECTED = (
        'move(2,3)' +  ' ' +
        'move(3,2)' + '   ' +
        'move(4,3)' +  ' '
    )
    assert str(Shape.CircleFill(3, 3, 1)) == EXPECTED
    assert str(Shape.CircleFill(3, 3, sqrt(2) - EPSILON)) == EXPECTED

def test_circlefill_radius_sqrt_2():
    #                           ###
    # sqrt(2) <= r < 2:         ###
    #                           ###
    EXPECTED = (
        'move(2,2)' + '   ' +
        'move(3,2)' + '   ' +
        'move(4,2)' + '   '
    )
    assert str(Shape.CircleFill(3, 3, sqrt(2))) == EXPECTED
    assert str(Shape.CircleFill(3, 3, 2 - EPSILON)) == EXPECTED

def test_circlefill_radius_2():
    #                            #
    #                           ###
    # 2 <= r < sqrt(5):        #####
    #                           ###
    #                            #
    EXPECTED = (
        'move(1,3)' +   ' ' +
        'move(2,2)' +  '   ' +
        'move(3,1)' + '     ' +
        'move(4,2)' +  '   ' +
        'move(5,3)' +   ' '
    )
    assert str(Shape.CircleFill(3, 3, 2)) == EXPECTED
    assert str(Shape.CircleFill(3, 3, sqrt(5) - EPSILON)) == EXPECTED

def test_circlefill_radius_sqrt_5():
    #                           ###
    #                          #####
    # sqrt(5) <= r < sqrt(8):  #####
    #                          #####
    #                           ###
    EXPECTED = (
        'move(1,2)' +  '   ' +
        'move(2,1)' + '     ' +
        'move(3,1)' + '     ' +
        'move(4,1)' + '     ' +
        'move(5,2)' +  '   '
    )
    assert str(Shape.CircleFill(3, 3, sqrt(5))) == EXPECTED
    assert str(Shape.CircleFill(3, 3, sqrt(8) - EPSILON)) == EXPECTED

