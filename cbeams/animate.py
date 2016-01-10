import math
import random
import sys
import time

from . import shape, terminal

class Firework():
    '''
    A firework looks like an expanding annulus.
    (i.e. a colored circle with a hole in the middle).
    '''
    def __init__(self):
        # Center point.
        self.y, self.x = terminal.rand_coord()

        self.color = terminal.rand_color()

        # The max radius we will reach.
        self.size = 2 + min(100, random.expovariate(0.2))

        # How close 'outer' gets to its max size before 'inner' starts to grow.
        # From 0 to 1
        self.thickness = random.triangular(0.2, 0.95)

        # Outer and inner radii.
        self.outer = 0.0
        self.inner = 0.0
        # The value of 'inner' on the last frame.
        self.inner_last = self.inner

    def update(self):
        if self.outer < self.size * 0.95:
            self.outer += (self.size - self.outer) * 0.08
        if self.outer > self.size * self.thickness:
            self.inner_last = self.inner
            self.inner += (self.size - self.inner) * 0.08

    @property
    def deleteme(self):
        return self.inner > self.outer

    def draw(self):
        # Draw the full coloured annulus from inner to outer radii.
        sys.stdout.write(self.color)
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.outer, self.inner)
        ))
        # Draw a very thin background colored annulus just inside 'inner',
        # to erase the innermost part of the last frame's annulus.
        sys.stdout.write(terminal.terminal.on_color(0))
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.inner, self.inner_last)
        ))

def should_add_new_item(elapsed):
    return random.random() < -math.cos(elapsed / 3) / 2 + 0.6

def animate():
    world = set()
    start_time = time.time()
    while True:
        start_frame = time.time()
        elapsed = start_frame - start_time
        if should_add_new_item(elapsed):
            world.add(Firework())
        for item in world:
            item.update()
        for item in [item for item in world if item.deleteme]:
            world.remove(item)
        for item in world:
            item.draw()
        sys.stdout.flush()
        time.sleep(max(0, 1/60 + start_frame - time.time()))

