import contextlib
import sys
import time

from blessings import Terminal

terminal = Terminal()

class Shape():

    def __init__(self, color, slivers):
        self.color = color
        self.slivers = slivers

    def __str__(self):
        return self.color + ''.join(
            terminal.move(y, x) + ' ' * length
            for y, x, length in self.slivers
        )

def rectfill(y1, x1, y2, x2):
    return [
        (y, x1, x2 - x1)
        for y in range(y1, y2)
    ]


def reset_on_exit(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        with terminal.location():
            func(*args, **kwargs)
        print(terminal.normal)

    return inner

@contextlib.contextmanager
def reset_on_exit():
    with terminal.location():
        try:
            yield
        finally:
            print(terminal.normal)

def animate():
    with reset_on_exit():
        for size in range(terminal.height // 2 + 1):
            shape = Shape(
                terminal.on_blue,
                rectfill(
                    terminal.height // 2 - size,
                    terminal.width // 2 - size,
                    size * 2 + 1,
                    size * 2 + 1
            ))
            print(str(shape), sep='', end='')
            sys.stdout.flush()
            time.sleep(0.02)

