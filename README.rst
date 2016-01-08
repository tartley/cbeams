cbeams
======

A command-line program which draws pretty animated colored circles in the
terminal.

Dependencies
------------

Developed on on Ubuntu 14.04.

Likely runs on other Linux.

Might work on OSX.

Will not work on Windows. The 'cmd' terminal does not accept ANSI terminal
codes. Could probably be made to work on Windows using 'colorama', or ansi.sys,
but I don't have a Windows machine, and don't plan on doing that.

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
* README should include a link to the binary release(s?)
* Can README embed that ascii cinema thing?
  If not, embed a screenshot and link to it.
* Test on OSX
* Create a redistributable binary for OSX
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

