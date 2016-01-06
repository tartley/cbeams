from contextlib import contextmanager
import functools

from blessings import Terminal

terminal = Terminal()

@contextmanager
def reset_on_exit():
    try:
        yield
    finally:
        print(terminal.cnorm + terminal.normal)

