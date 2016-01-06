import math
import random
import sys
import time

from blessings import Terminal

from . import shape, terminal

class Annulus():

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.color = terminal.rand_color()
        self.radius = 1.0
        self.growth = 1.4
        self.deleteme = False

    def update(self):
        self.radius += self.growth
        self.growth /= 1.1
        if self.growth < 0.01:
            self.deleteme = True

    def draw(self):
        sys.stdout.write(self.color)
        sys.stdout.write(terminal.render(
            shape.disc(self.y, self.x, self.radius)
        ))


def animate():
    world = set([Annulus(*terminal.center())])
    start = time.time()
    last = 0
    while True:
        elapsed = time.time() - start
        if elapsed - last > 0.25:
            world.add(Annulus(*terminal.rand_coord()))
            last = elapsed
        for item in world:
            item.update()
        for item in [item for item in world if item.deleteme]:
            world.remove(item)
        for item in world:
            item.draw()
        sys.stdout.flush()
        time.sleep(0.02)

