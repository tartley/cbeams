import functools
import math
import sys
import time

from blessings import Terminal

from .shape import Shape
from .render import render

terminal = Terminal()

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
    MAX_RADIUS = math.trunc(
        math.sqrt(
            (terminal.height / 2) ** 2 +
            (terminal.width  / 2) ** 2
        )
    ) + 1
    STEPS = 10
    for step in range(0, MAX_RADIUS * STEPS):
        radius = step / STEPS
        shape = Shape.CircleFill(
            terminal.height // 2, terminal.width // 2, radius
        )
        print(
            color, render(terminal, shape), terminal.move(0, 0),
            sep='', end=''
        )
        sys.stdout.flush()
        time.sleep(0.02)

