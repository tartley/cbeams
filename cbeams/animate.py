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
        (terminal.on_blue,    Shape.RectFill(1, 1, 1, 1)),
        (terminal.on_magenta, Shape.RectFill(-3, 1, -2, 1)),
        (terminal.on_green,   Shape.RectFill(1, -3, 1, -2)),
        (terminal.on_red,     Shape.RectFill(-3, -3, -2, -2)),
    ]:
        print(color, str(shape), sep='', end='')
        sys.stdout.flush()

