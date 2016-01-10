import sys

from . import animate, cmdline, terminal

def main():
    '''
    Application console script entry point, referenced from setup.py
    '''
    opts = cmdline.parse(sys.argv[1:])
    with terminal.reset_on_exit(opts['--overwrite']):
        animate.animate()


if __name__ == '__main__':
    main()

