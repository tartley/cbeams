TODO
----
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

