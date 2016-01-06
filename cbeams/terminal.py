from contextlib import contextmanager
import functools

from blessings import Terminal

terminal = Terminal()

@contextmanager
def reset_on_exit():
    print(terminal.civis)
    try:
        yield
    except KeyboardInterrupt:
        pass
    finally:
        print(terminal.cnorm + terminal.normal)

def clip(strips):
    '''
    Yield a sequence of strips after clipping them to (0, 0) to (height, width).
    '''
    for y, x, length in strips:
        if not(0 <= y < terminal.height):
            continue
        if x < 0:
            length += x
            x = 0
        if length + x > terminal.width:
            length = terminal.width - x
        if length > 0:
            yield y, x, length


def render(shape):
    return ''.join(
        terminal.move(y, x) + ' ' * length
        for y, x, length in clip(shape.strips)
    )

