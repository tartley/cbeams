import math
import random
import sys
import time

from blessings import Terminal

from . import shape, terminal

class Firework():
    '''
    A firework looks like an annulus (ring), but is actually drawn as *two*
    annuli - one broad colored one, with a thinner black one within it to
    erase the color as the ring expands.
    '''

    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.color = terminal.rand_color()
        self.max = random.uniform(1.4, 4) ** 2
        self.thickness = random.uniform(0.1, 0.9)
        self.outer = 0.0
        self.inner = 0.0
        self.inner_last = self.inner

    def update(self):
        if self.outer < self.max * 0.95:
            self.outer += (self.max - self.outer) * 0.1
        if self.outer > self.max * self.thickness:
            self.inner_last = self.inner
            self.inner += (self.max - self.inner) * 0.1

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
        time.sleep(0.01)

