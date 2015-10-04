import sys

from . import cmdline


def main():
    '''
    Application console script entry point.
    '''
    cmdline.parse(sys.argv[1:])
    print('Hello, World.')


if __name__ == '__main__':
    main()

