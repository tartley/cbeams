import math
import sys
import time

from blessings import Terminal

from . import shape
from .terminal import render

terminal = Terminal()

def animate():
    MAX_RADIUS = math.trunc(
        math.sqrt(
            (terminal.height / 2) ** 2 +
            (terminal.width  / 2) ** 2
        )
    ) + 1
    radius = 1.0
    color = terminal.on_red
    while radius < MAX_RADIUS:
        strips = shape.disc(
            terminal.height // 2, terminal.width // 2, radius
        )
        print(color, render(strips), sep='', end='')
        sys.stdout.flush()
        time.sleep(0.02)
        radius *= 1.02

