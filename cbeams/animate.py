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
        self.outer = 0.0
        self.outer_last = self.outer

    def update(self):
        self.outer_last = self.outer
        self.outer += (self.max - self.outer) * 0.1

    @property
    def deleteme(self):
        return self.max - self.outer < 0.01

    def draw(self):
        sys.stdout.write(self.color)
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.outer, self.outer_last)
        ))

def get_new_firework():
    return Firework(*terminal.rand_coord())

def animate():
    world = set([Firework(*terminal.center())])
    start = time.time()
    last = 0
    while True:
        elapsed = time.time() - start
        if elapsed - last > 0.05:
            world.add(get_new_firework())
            last = elapsed
        for item in world:
            item.update()
        for item in [item for item in world if item.deleteme]:
            world.remove(item)
        for item in world:
            item.draw()
        sys.stdout.flush()

