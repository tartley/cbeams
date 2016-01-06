import sys

from . import animate, cmdline, terminal

def main():
    '''
    Application console script entry point.
    '''
    cmdline.parse(sys.argv[1:])
    with terminal.reset_on_exit():
        animate.animate()


if __name__ == '__main__':
    main()

