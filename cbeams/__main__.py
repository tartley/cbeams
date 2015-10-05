import sys

from . import cmdline, terminal

def main():
    '''
    Application console script entry point.
    '''
    cmdline.parse(sys.argv[1:])
    terminal.animate()


if __name__ == '__main__':
    main()

