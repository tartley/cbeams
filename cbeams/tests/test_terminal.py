from unittest.mock import Mock, patch

from ..terminal import clip, render

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
    strips = [(1, 2, 3), (4, 5, 6)]
    assert render(strips) == \
        'move(1,2)' + ' ' * 3 + \
        'move(4,5)' + ' ' * 6

@patch('cbeams.terminal.terminal', get_mock_terminal())
def test_render_should_clip():
    strips = [(1, -2, 26)]
    assert render(strips) == 'move(1,0)' + ' ' * 22


@patch('cbeams.terminal.terminal', Mock(height=99, width=10))
def test_clip_left():
    strips = [
        (1, 0, 10), # not clipped
        (2, -2, 6), # clipped to length 4
        (3, -4, 5), # clipped to length 1
        (4, -6, 6), # clipped to length 0, i.e. removed entirely
    ]
    assert list(clip(strips)) == [
        (1, 0, 10),
        (2, 0, 4),
        (3, 0, 1),
    ]

@patch('cbeams.terminal.terminal', Mock(height=99, width=10))
def test_clip_right():
    strips = [
        (1, 0, 10), # not clipped
        (2, 0, 11), # clipped to length 10
        (3, 9, 99), # clipped to length 1
        (4, 10, 99), # clipped to length 0, i.e. removed entirely
    ]
    assert list(clip(strips)) == [
        (1, 0, 10),
        (2, 0, 10),
        (3, 9, 1),
    ]

@patch('cbeams.terminal.terminal', Mock(height=10, width=99))
def test_clip_top_and_bottom():
    strips = [
        (-1, 0, 10), # removed entirely
        (0, 0, 10), # not clipped
        (9, 0, 10), # not clipped
        (10, 0, 10), # removed entirely
    ]
    assert list(clip(strips)) == [
        (0, 0, 10),
        (9, 0, 10),
    ]

