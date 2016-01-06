from unittest.mock import Mock, patch

from ..shape import Shape
from ..terminal import render

def get_mock_terminal(**overrides):
    attrs = dict(
        move='move({},{})'.format,
        height=11,
        width=22,
    )
    attrs.update(overrides)
    return Mock(**attrs)

@patch('cbeams.terminal.terminal', get_mock_terminal())
def test_render():
    shape = Shape([(1, 2, 3), (4, 5, 6)])
    assert render(shape) == \
        'move(1,2)' + ' ' * 3 + \
        'move(4,5)' + ' ' * 6

@patch('cbeams.terminal.terminal', get_mock_terminal())
def test_render_should_clip():
    shape = Shape([(1, -2, 26)])
    assert render(shape) == 'move(1,0)' + ' ' * 22


