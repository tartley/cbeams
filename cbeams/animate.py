import math
import random
import sys
import time

from blessings import Terminal

from . import shape, terminal

class Firework():

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.color = terminal.rand_color()
        self.max = random.uniform(5, 20)
        self.inner = 1.0

    def update(self):
        self.inner += (self.max - self.inner) * 0.1

    @property
    def deleteme(self):
        return self.max - self.inner < 0.01

    def draw(self):
        sys.stdout.write(self.color)
        sys.stdout.write(terminal.render(
            shape.disc(self.y, self.x, self.inner)
        ))


def animate():
    world = set([Firework(*terminal.center())])
    start = time.time()
    last = 0
    while True:
        elapsed = time.time() - start
        if elapsed - last > 0.25:
            world.add(Firework(*terminal.rand_coord()))
            last = elapsed
        for item in world:
            item.update()
        for item in [item for item in world if item.deleteme]:
            world.remove(item)
        for item in world:
            item.draw()
        sys.stdout.flush()
        time.sleep(0.02)

