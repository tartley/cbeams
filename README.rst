cbeams
======

`cbeams` is a command-line program which draws pretty colored things in the
terminal.

    I've seen things you people wouldn't believe. Attack ships on fire off the
    shoulder of Orion. I watched c-beams glitter in the dark, near the
    Tannhäuser Gate. All those moments will be lost, in time, like tears in
    rain. Time to die.

Dependencies
------------

Python >= 3.5. Probably runs on earlier v3.x, but I haven't tried it.

Install
-------

::

    pip install cbeams

Usage
-----

See `cbeams -h`.

Immediate Future Plans
----------------------
* Move the Shape to string conversion out of `shape`, and delete that module's
  usage of `terminal`.
* Do the display of all objects using a single 'print' function, presumably
  by aggregating all output into a single StringIO.
* Clip all shapes to the terminal size before rendering
    Check: Can we print at bottom right without causing scrolling?
* Run until a key is pressed
* Draw a shape which restores the original text/color.
* Draw an expanding colored circle, with a restoring circle within it,
  until the terminal is restored to its original state.
* Create a wheel on PyPI
    Using 'twine'? See https://packaging.python.org
    Using setup.cfg instead of setup.py?
    Backport this into python-app template
* Create a redistributable binary for Linux
    Backport this into python-app template
* Create a redistributable binary for OSX
    Backport this into python-app template
* Run on Windows, using colorama
* Create a redistributable binary for Windows
    Backport this into python-app template
* Draw an annulus - one circle subtracted from another.
  Presumably we can speed up the animation using this?
  First profile & measure how many simultaneous circles we can animate.

Speculative Future Ideas
------------------------
* Quick poll of aspect ratio of various fonts in various terminals
* Double buffering?
* 256 colors?
* Make a noise

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

To the processes or influences that resulted in the creation of our universe
and the emergence within it of complexity, life, and intelligence.

Contact
-------

:For users: Downloads & documentation:
    http://pypi.python.org/pypi/cbeams/

:For developers: Souce code & issues:
    https://github.com/tartley/cbeams/

:Contact the author:
    Jonathan Hartley, email: tartley at domain tartley.com, Twitter: @tartley.

