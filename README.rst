cbeams
======

A command-line program which draws pretty animated colored circles in the
terminal.

.. image:: screenshots/cbeams.png

    *I've seen things you people wouldn't believe. Attack ships on fire off the
    shoulder of Orion. I watched c-beams glitter in the dark, near the
    Tannhäuser Gate. All those moments will be lost, in time, like tears in
    rain. Time to die.*

Downloading as a binary executable
----------------------------------

A Linux binary executable can be downloaded from:

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

