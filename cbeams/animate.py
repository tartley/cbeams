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
    def __init__(self, color):
        self.color = color # as an integer

        # Center point.
        self.y, self.x = terminal.rand_coord()

        # The max radius we will reach.
        term_size = terminal.get_max_dimension()
        self.size = 2 + min(term_size * 2, random.expovariate(32 / term_size))

        # How close 'outer' gets to its max size before 'inner' starts to grow.
        # From 0 to 1
        self.thickness = random.triangular(0.3, 0.95)

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
        sys.stdout.write(terminal.on_color(self.color))
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.outer, self.inner)
        ))
        # Draw a very thin background colored annulus just inside 'inner',
        # to erase the innermost part of the last frame's annulus.
        sys.stdout.write(terminal.normal)
        sys.stdout.write(terminal.render(
            shape.annulus(self.y, self.x, self.inner, self.inner_last)
        ))

class Generator():
    '''
    Generates new Fireworks to be added into the world
    '''
    def __init__(self):
        self.colors = [self._rand_color()]

    def _rand_color(self):
        return random.randint(1, terminal.number_of_colors - 1)

    def get_new_items(self, elapsed):
        # possibly add or remove an allowable color
        value = random.random()
        if value < 0.01 and len(self.colors) < 4:
            self.colors.append(self._rand_color())
        elif value < 0.02 and len(self.colors) > 1:
            self.colors.pop(0)

        # possibly generate a new Firework
        if random.random() < -math.cos(elapsed / 3) / 2 + 0.6:
            return [Firework(color=random.choice(self.colors))]
        else:
            return []

def update(generator, world, elapsed):
    for item in generator.get_new_items(elapsed):
        world.add(item)
    delete = []
    for item in world:
        item.update()
        if item.deleteme:
            delete.append(item)
    for item in delete:
        world.remove(item)

def draw(world):
    for item in world:
        item.draw()
    sys.stdout.flush()

def limit_framerate(start_frame):
    time.sleep(max(0, 1/60 + start_frame - time.time()))

def animate():
    world = set()
    generator = Generator()
    start_time = time.time()
    while True:
        start_frame = time.time()
        update(generator, world, start_frame - start_time)
        draw(world)
        limit_framerate(start_frame)

