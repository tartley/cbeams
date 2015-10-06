import functools
import sys
import time

from blessings import Terminal

from .shape import Shape

terminal = Terminal()
Shape.terminal = terminal

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
    for color, shape in [
        (terminal.on_blue, Shape.rectfill(1, 1, 2, 2)),
        (
            terminal.on_magenta,
            Shape.rectfill(terminal.height - 3, 1, terminal.height - 1, 2)
        ),
        (
            terminal.on_green,
            Shape.rectfill(
                1, terminal.width - 3, 2, terminal.width - 1,
            )
        ),
        (
            terminal.on_red,
            Shape.rectfill(
                terminal.height - 3, terminal.width - 3,
                terminal.height - 1, terminal.width - 1,
            )
        ),
    ]:
        print(color, str(shape), sep='', end='')
        sys.stdout.flush()

