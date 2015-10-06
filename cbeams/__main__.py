import sys

from . import cmdline, animate

def main():
    '''
    Application console script entry point.
    '''
    cmdline.parse(sys.argv[1:])
    animate.animate()


if __name__ == '__main__':
    main()

