import math
import random
import sys
import time

from blessings import Terminal

from . import shape, terminal

class Firework():
    '''
    A firework looks like an expanding annulus.
    (i.e. a ring, a colored circle with a black hole in the middle).
    '''
    def __init__(self):
        # Center point
        self.y, self.x = terminal.rand_coord()

        self.color = terminal.rand_color()

        # The max radius we will reach
        self.max = 2 + min(100, random.expovariate(0.2))

        # How close 'outer' gets to max before inner hole appears
        self.thickness = random.triangular(0.2, 0.95)

        # Outer and inner radius
        self.outer = 0.0
        self.inner = 0.0
        # The value of 'inner' on the last frame
        self.inner_last = self.inner

    def update(self):
        if self.outer < self.max * 0.95:
            self.outer += (self.max - self.outer) * 0.08
        if self.outer > self.max * self.thickness:
            self.inner_last = self.inner
            self.inner += (self.max - self.inner) * 0.08

    @property
    def deleteme(self):
        return self.inner > self.outer

    def draw(self):
        sys.stdout.write(self.color)
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.outer, self.inner)
        ))
        sys.stdout.write(terminal.terminal.on_black)
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.inner, self.inner_last)
        ))

def animate():
    world = set()
    start = time.time()
    last = 0
    while True:
        elapsed = time.time() - start
        if elapsed - last > 0.02:
            world.add(Firework())
            last = elapsed
        for item in world:
            item.update()
        for item in [item for item in world if item.deleteme]:
            world.remove(item)
        for item in world:
            item.draw()
        sys.stdout.flush()
        time.sleep(0.01)

