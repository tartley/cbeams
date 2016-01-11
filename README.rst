cbeams
======

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

Tested on Python 3.4 & 3.5. Probably also runs on other 3.x, but not on 2.x.

Python dependencies are specified in setup.py.

Installing
..........

::

    pip install cbeams

Usage
-----

See `cbeams -h`.

Immediate Future Plans
----------------------
* Screenshot in the README
* release v1.1.0
* Create a 32-bit Linux redistributable
* release v1.2.0
* Test on OSX
* Create a redistributable binary for OSX
* release v1.3.0
* Try colorama, just in case it works
* If so, create redistributable binary for Windows
* Release v1.4.0
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

