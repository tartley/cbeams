from unittest.mock import Mock

from ..shape import Shape
from ..render import render

def get_mock_terminal(**overrides):
    attrs = dict(
        move=lambda x, y: 'move({},{})'.format(x, y),
        height=11,
        width=22,
    )
    attrs.update(overrides)
    return Mock(**attrs)

def test_render():
    shape = Shape([(1, 2, 3), (4, 5, 6)])
    assert render(get_mock_terminal(), shape) == (
        'move(1,2)' + ' ' * 3 +
        'move(4,5)' + ' ' * 6
    )

def test_render_clips_left():
    shape = Shape([
        (1, 0, 2),  # not clipped
        (2, -2, 6), # clipped to length 4
        (3, -4, 5), # clipped to length 1
        (4, -6, 6), # clipped to length 0, i.e. removed entirely
    ])
    assert render(get_mock_terminal(), shape) == (
        'move(1,0)' + ' ' * 2 +
        'move(2,0)' + ' ' * 4 +
        'move(3,0)' + ' ' * 1
    )

