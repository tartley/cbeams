cbeams
======

I've seen things you people wouldn't believe. Attack ships on fire off the
shoulder of Orion. I watched c-beams glitter in the dark, near the Tannhäuser
Gate. All those moments will be lost, in time, like tears in rain. Time to die.

A command-line program which draws pretty animated colored circles in the
terminal.

Developed on on Ubuntu 14.04, likely runs on other Linux.

Might run on OSX. Does not run on Windows.

Downloading as a binary executable
----------------------------------

If you're on 64-bit Linux, you can download a binary executable that should
just work:

    https://github.com/tartley/cbeams/releases

Open a terminal, tar -xzf the release, and run the script 'cbeams'.

Downloading as source
---------------------

Dependencies
............

Works on Linux or OSX, but not on Windows.

Tested on Python 3.4 & 3.5. Probably also runs on other 3.x, but not on 2.x.

Python dependencies are specified in setup.py.

Installing
..........

::

    pip install cbeams

Usage
-----

See `cbeams -h`.

TODO
----
* put make exe-linux into a script?
* Fix make exe-linux hardcoded values:
    For name, we can assume the project templating will do it
    For version, we cannot, it must be derived at runtime,
        Review that section in PPA docs about places to put version number
        Use a new script to get them from our existing source?
        Run our program to get them?
        Get them from env vars?
* Screenshot in the README
* Try PyInstaller 3.1
* Create a final release:
    set version number
    tag
* Create a redistributable binary for OSX
    64 bit is fine? Is there no longer any such thing as a 32-bit modern OSX?
* Try colorama, just in case it works
* If so, create 32 bit redistributable binary for Windows
    Beware PyInstaller 3.1 bug:
        Apps built with Windows 10 and Python 3.5 may not run on earlier
        Windows versions
* Backport into my python-app template:
    * wheel creation
    * python3.5.1
    * Linux binary redistributable
    * OSX binary redistributable
    * Windows binary redistributable

Hacking
-------

To populate a virtualenv, run tests, etc, see the commands in the Makefile.
These can often work in Windows too, under Bash shells like Cygwin, Msys.

Populating the virtualenv in the manner shown in the Makefile will also
add "-e ." to the virtualenv, which adds this project in 'develop mode',
meaning both that source edits are immediately visible within the virtualenv,
and that the application entry points listed in setup.py are converted into
executable scripts on the PATH.

Thanks
------

To Erik Rose, for the fabulous Blessings package.
https://pypi.python.org/pypi/blessings

Links & Contact
---------------

:Python package:
    http://pypi.python.org/pypi/cbeams/

:Binaries, source, issues:
    https://github.com/tartley/cbeams/

:Author:
    Jonathan Hartley, email: tartley at domain tartley.com, Twitter: @tartley.

