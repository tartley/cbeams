from unittest.mock import Mock

import pytest

from ..shape import Shape

def get_mock_terminal(**overrides):
    attrs = dict(
        move=lambda x, y: 'move({},{})'.format(x, y),
        height=11,
        width=22,
    )
    attrs.update(overrides)
    return Mock(**attrs)

def test_constructor():
    shape = Shape('slivers')
    assert shape.slivers == 'slivers'

def test_str():
    shape = Shape([(1, 2, 3), (4, 5, 6)])
    shape.terminal = get_mock_terminal()
    assert str(shape) == 'move(1,2)' + ' ' * 3 + 'move(4,5)' + ' ' * 6

def test_rectfill():
    '''
         x
         012345
      y 0 ####
        1 ####
        2 ####
        3
        4
    '''
    assert Shape.RectFill(get_mock_terminal(), 0, 1, 2, 4).slivers \
        == [(0, 1, 4), (1, 1, 4), (2, 1, 4)]

def test_rectfill_should_work_on_minimal():
    assert Shape.RectFill(get_mock_terminal(), 1, 1, 1, 1).slivers \
        == [(1, 1, 1)]

def test_rectfill_with_negative_coords_should_interpret_from_right_bottom():
    '''
         x
         012345
      y 0
        1   ###
        2   ###
        3   ###
        4
    '''
    shape = Shape.RectFill(get_mock_terminal(height=5, width=6), -4, -3, -2, -1)
    assert shape.slivers == [(1, 3, 3), (2, 3, 3), (3, 3, 3)]

def test_rectfill_with_unordered_args_should_raise():
    with pytest.raises(ValueError):
        Shape.RectFill(get_mock_terminal(), 1, 1, 0, 1)
    with pytest.raises(ValueError):
        Shape.RectFill(get_mock_terminal(), 1, 1, 1, 0)

