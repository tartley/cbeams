from unittest.mock import Mock

from ..shape import Shape
from ..render import render

def get_mock_terminal(**overrides):
    attrs = dict(
        move='move({},{})'.format,
        height=11,
        width=22,
    )
    attrs.update(overrides)
    return Mock(**attrs)

def test_render():
    shape = Shape([(1, 2, 3), (4, 5, 6)])
    assert render(get_mock_terminal(), shape) == \
        'move(1,2)' + ' ' * 3 + \
        'move(4,5)' + ' ' * 6

def test_render_should_clip():
    shape = Shape([(1, -2, 26)])
    assert render(get_mock_terminal(), shape) == 'move(1,0)' + ' ' * 22

