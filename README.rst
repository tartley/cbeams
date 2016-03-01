cbeams
======

I've seen things you people wouldn't believe. Attack ships on fire off the
shoulder of Orion. I watched c-beams glitter in the dark, near the Tannhäuser
Gate. All those moments will be lost, in time, like tears in rain. Time to die.

A command-line program which draws pretty animated colored circles in the
terminal.

Downloading as a binary executable
----------------------------------

A 32-bit Linux binary executable can be downloaded from:

    https://github.com/tartley/cbeams/releases

You don't need any version of Python installed, just download, open a terminal,
tar -xzf the release, and run the script 'cbeams'.

Downloading as source
---------------------

Dependencies
............

Developed on on Ubuntu 14.04, likely works on other Linux.
Does work on OSX.
Does not work on Windows.

Tested on Python 3.4 & 3.5. Probably also runs on other 3.x.
Does not run on 2.x.

Python dependencies are specified in setup.py.

Installing
..........

::

    pip install cbeams

Usage
-----

Just run `cbeams`. For options, see `cbeams -h`.

TODO
----
* Screenshot in the README
* Add the binaries to a new 1.0.0 release
* Should my Linux binary builds use an old version of ubuntu? (i.e 14.04?)
    * test the binary on a fresh 14.04 ubuntu install
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
    * setup.py unicode reading of README, etc.
    * bin/make-exe

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

