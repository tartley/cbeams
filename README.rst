cbeams
======

A command-line program which draws pretty animated colored circles in the
terminal.

    *I've seen things you people wouldn't believe. Attack ships on fire off the
    shoulder of Orion. I watched c-beams glitter in the dark, near the
    Tannhäuser Gate. All those moments will be lost, in time, like tears in
    rain. Time to die.*

.. image:: screenshots/cbeams.png

It looks better animated than a static screenshot conveys. You should
download and run it!

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

::

    cbeams [-o]
    cbeams [-h]

    -o  Overwrites one screenful of the existing terminal contents
    -h  Displays help.

Why did I develop this?
-----------------------

The traditional way to do colors or animation in a terminal is to use the
venerable UNIX library 'curses', or its open source clone 'ncurses'. There are
many Python packages that expose ncurses for various uses. Anyone who has used
these knows that curses is a definite contender for one of the worst APIs in
existence. It systematically exposes callers to reams of the incidental
complexity of the underlying implementation, accumulated by supporting decades
of generations of different terminals and terminal emulators.

Fortunately, nowadays there is a better way. Erik Rose's 'Blessings' package
layers a sane API on top of ncurses. The documentation page shows how 21 lines
of incomprehensible code using curses is transformed into four straightforward
lines of code using blessings.

I wanted an excuse to learn how blessings works, and cbeams is the result.
I tag it onto the end of long-running commands to use as a visual notification
that the command has finished.

Pressing ctrl-C exits cbeams, flipping back to the regular terminal buffer, so
the animation doesn't overwrite any of your previous output.

For fun, there's also a '-o' arg, which overwrites the terminal text without
flipping buffers. So you can see the expanding circles slowly eat away at your
existing terminal text, but then when you ctrl-c, it's not possible to restore
the terminal. So one screenful of your terminal text is overwritten and lost. 

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

