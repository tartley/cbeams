import functools
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
            try:
                func(*args, **kwargs)
            finally:
                print(terminal.normal)
    return inner

@reset_on_exit
def animate():
    for shape in [
        Shape(terminal.on_blue, rectfill(1, 1, 2, 2)),
        Shape(
            terminal.on_magenta,
            rectfill(
                terminal.height - 3, 1, terminal.height - 1, 2
            )
        ),
        Shape(
            terminal.on_green,
            rectfill(
                1, terminal.width - 3, 2, terminal.width - 1,
            )
        ),
        Shape(
            terminal.on_red,
            rectfill(
                terminal.height - 3, terminal.width - 3,
                terminal.height - 1, terminal.width - 1,
            )
        ),
    ]:
        print(str(shape), sep='', end='')
        sys.stdout.flush()

