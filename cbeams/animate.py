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
    color = terminal.on_blue
    for step in range(0, min(terminal.height, terminal.width) * 10 // 2):
        radius = step / 10
        shape = Shape.CircleFill(
            terminal.height // 2, terminal.width // 2, radius
        )
        print(color, str(shape), terminal.move(0, 0), sep='', end='')
        sys.stdout.flush()
        time.sleep(0.02)

