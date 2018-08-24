# I don't know how to make PyInstaller use the setuptools entry point (in
# __main__.py) This file exists to provide a top level script PyInstaller
# can operate on.

from cbeams.__main__ import main

if __name__ == '__main__':
    main()

