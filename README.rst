cbeams
======

A command-line program which draws pretty animated colored circles in the
terminal.

Binary installs
---------------

If you're on 64-bit Linux, you can run cbeams by downloading a binary that
should just work:

    https://github.com/tartley/cbeams/releases

Open a terminal, tar -xzf the release, and run the script 'cbeams'.

On 32-bit Linux, or on OSX, read on.

Dependencies
------------

Developed on on Ubuntu 14.04, likely runs on other Linux.

Might work on OSX.

Doesn't work on Windows, which doesn't interpret ANSI sequences in its
terminal. This could probably be made to work using 'colorama', or ansi.sys.

Tested on Python 3.4 & 3.5. Probably also runs on other 3.x, but not on 2.x.

Python dependencies are specified in setup.py.

Install
-------

::

    pip install cbeams

Usage
-----

See `cbeams -h`.

Immediate Future Plans
----------------------
* Can README embed that ascii cinema thing?
  If not, embed a screenshot and link to it.
* Test on OSX
* Create a redistributable binary for OSX
* Consider a 32 bit VM or chroot to build 32 binary redistributables.
* Backport wheel creation into my python-app template
* Backport python3.5.1 to my python-app template
* Backport Linux redistributable binary to my python-app template
* Backport OSX redistributable binary to my python-app template

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

Contact
-------

:For users: Downloads & documentation:
    http://pypi.python.org/pypi/cbeams/

:For developers: Souce code & issues:
    https://github.com/tartley/cbeams/

:Author:
    Jonathan Hartley, email: tartley at domain tartley.com, Twitter: @tartley.

