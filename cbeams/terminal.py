import contextlib
import sys
import random

from blessings import Terminal

terminal = Terminal()

@contextlib.contextmanager
def noop():
    yield

def on_entry(overwrite):
    sys.stdout.write(terminal.civis + terminal.normal)
    if not overwrite:
        sys.stdout.write(terminal.clear)

def on_exit(overwrite):
    if overwrite:
        # move cursor to bottom of terminal
        sys.stdout.write(terminal.move(terminal.height - 1, 0))
    sys.stdout.write(terminal.cnorm + terminal.normal)

@contextlib.contextmanager
def reset_on_exit(overwrite):
    try:
        with (noop if overwrite else terminal.fullscreen)():
            on_entry(overwrite)
            yield
    except KeyboardInterrupt:
        pass
    finally:
        on_exit(overwrite)


def center():
    return terminal.height // 2, terminal.width // 2

def rand_coord():
    return (
        random.randint(0, terminal.height - 1),
        random.randint(0, terminal.width - 1)
    )


def clip(strips):
    '''
    Yield a sequence of strips after clipping them to (0, 0), (height, width).
    (inclusive)
    '''
    for y, x, length in strips:
        if y < 0 or y >= terminal.height:
            continue
        if x < 0:
            length += x
            x = 0
        if length + x > terminal.width:
            length = terminal.width - x
        if length > 0:
            yield y, x, length

def render(strips):
    return ''.join(
        terminal.move(y, x) + ' ' * length
        for y, x, length in clip(strips)
    )

on_color = terminal.on_color

number_of_colors = terminal.number_of_colors

normal = terminal.normal

