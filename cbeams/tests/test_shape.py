from unittest.mock import Mock, patch

import pytest

from ..shape import Shape

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
    '''
         012345 x
      y 0 ####
        1 ####
        2 ####
        3
        4
    '''
    assert str(Shape.RectFill(0, 1, 2, 4)) == ( \
        'move(0,1)' + ' ' * 4 +
        'move(1,1)' + ' ' * 4 +
        'move(2,1)' + ' ' * 4
    )

def test_rectfill_should_handle_minimal_case():
    assert str(Shape.RectFill(1, 1, 1, 1)) == 'move(1,1) '

def test_rectfill_with_unordered_args_should_raise():
    with pytest.raises(ValueError):
        Shape.RectFill(1, 1, 0, 1)
    with pytest.raises(ValueError):
        Shape.RectFill(1, 1, 1, 0)


def test_circlefill():
    assert str(Shape.CircleFill(2, 2, 2, aspect=1)) == (
        'move(1,1)' + ' ' * 3 +
        'move(2,0)' + ' ' * 5 +
        'move(3,1)' + ' ' * 3
    )

