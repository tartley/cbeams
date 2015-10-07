import functools
import math
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
            except KeyboardInterrupt:
                pass
            finally:
                print(terminal.normal)
    return inner

@reset_on_exit
def animate():
    start = time.time() / 4
    while True:
        radius = terminal.height / 4 * (1 - math.cos(time.time() / 4 - start))
        for color, shape in [
            (terminal.on_blue, Shape.RectFill(1, 1, 1, 1)),
            (terminal.on_magenta, Shape.RectFill(
                -3 % terminal.height, 1,
                -2 % terminal.height, 1
            )),
            (terminal.on_green, Shape.RectFill(
                1, -3 % terminal.width,
                1, -2 % terminal.width
            )),
            (terminal.on_red, Shape.RectFill(
                -3 % terminal.height, -3 % terminal.width,
                -2 % terminal.height, -2 % terminal.width
            )),
            (terminal.on_yellow,
                Shape.CircleFill(
                    terminal.height // 2,
                    terminal.width // 2,
                    radius)),
        ]:
            print(color, str(shape), sep='', end='')
        print(terminal.move(0, 0), end='')
        sys.stdout.flush()
        time.sleep(0.02)

