# This Makefile is just a cheatsheet to remind me of some commonly used
# commands. I'm generally executing these on OSX with up-to-date gnu binaries
# on the PATH, or on Ubuntu, or on WindowsXP/7 with Cygwin binaries foremost on
# the PATH.

# virtualenv

ve:
	# Make can't execute 'mkvirtualenv', 'cos we don't use interactive shell.
	# So execute it yourself:
	# mkvirtualenv -p $(which python3.5) -a . -r requirements-dev.txt cbeams

download-deps:
	pip install -r requirements.txt --download=deps
	rm deps/cbeams-*

popve:
	pip install -r requirements.txt --no-index --find-links=deps
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
	rm -rf build dist MANIFEST tags *.egg-info
	find . -name '*.py[oc]' -exec rm {} \;
.PHONY: clean

develop:
	# create executable entry points in our python or virtualenv's bin dir
	python setup.py develop
.PHONY: develop


# build a distributable

build:
	pyinstaller --name=cbeams cbeams/__main__.py


# push to PyPI

sdist: clean
	python setup.py sdist --formats=zip,gztar
.PHONY: sdist

register: clean
	python setup.py sdist --formats=zip,gztar register
.PHONY: register

upload: clean
	python setup.py sdist --formats=zip,gztar register upload
.PHONY: upload


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
