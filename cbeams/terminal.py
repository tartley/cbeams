from contextlib import contextmanager
import functools

from blessings import Terminal

terminal = Terminal()

@contextmanager
def reset_on_exit():
    try:
        yield
    finally:
        print(terminal.cnorm + terminal.normal)

def render(shape):
    return ''.join(
        terminal.move(y, x) + ' ' * length
        for y, x, length in shape.clipped(terminal.height, terminal.width)
    )

