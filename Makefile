# This Makefile is just a cheatsheet to remind me of some commonly used
# commands. I'm generally executing these on Ubuntu, but have in the past
# used them on OSX with up-to-date gnu binaries, or WindowsXP/7 with Cygwin
# binaries foremost on the PATH.

# virtualenv

ve:
	# Make can't execute this 'cos we don't use an interactive shell:
	# mkvirtualenv -p $$(which python3.5) -a . -r requirements-dev.txt cbeams

popve:
	pip install -r requirements-dev.txt


# development

test:
	py.test -q
.PHONY: test

pylint:
	pylint *.py
.PHONY: pylint

tags:
	ctags -R --languages=python .
.PHONY: tags

clean:
	rm -rf build dist MANIFEST tags *.egg-info *.spec
	find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean

develop:
	# create executable entry points in our python or virtualenv's bin dir
	pip install -e .
.PHONY: develop


# push to PyPI

sdist:
	python setup.py sdist --formats=gztar
.PHONY: sdist

# Pure Python wheel (since source does not support Python2)
wheel:
	python setup.py bdist_wheel
.PHONY: wheel

register:
	python setup.py register
.PHONY: register

upload: clean sdist wheel
	twine upload dist/*
.PHONY: upload


# build a redistributable binary
# TODO: Put this in a script.
# TODO: Hardcoded program name, program version, 32/64 bit ness
# TODO: try '${BASH_SOURCE%/*}'

exe-linux: clean
	pyinstaller main.py
	/bin/echo -e '#!/bin/bash\n$$(dirname $${BASH_SOURCE})/main/main\n' >dist/cbeams
	chmod a+x dist/cbeams
	(cd dist; tar -czf cbeams-linux-64bit-v1.0.0rc3.tar.gz cbeams main)

# Don't work

# profile:
#   # runsnake is a GUI visualiser for the output of cProfile
#   # http://www.vrplumber.com/programming/runsnakerun/
# 	python -O -m cProfile -o profile.out cbeams
# 	runsnake profile.out
# .PHONY: profile

# py2exe:
# 	rm -rf dist/cbeams-${RELEASE}.* build
# 	python setup.py --quiet py2exe
# .PHONY: py2exe
