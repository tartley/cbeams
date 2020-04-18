# This Makefile is just a cheatsheet to remind me of some commonly used
# commands. I'm generally executing these on Ubuntu, but have in the past
# used them on OSX with up-to-date gnu binaries, or WindowsXP/7 with Cygwin
# binaries foremost on the PATH.

# virtualenv

ve: ## Echo a command which can be used to create and populate a virtualenv
	@# Make can't execute this 'cos the shell it executes commands in
	@# isn't interactive, so doesn't have 'mkvirtualenv' available.
	@echo "You should execute this:"
	@echo 'mkvirtualenv -p $$(which python3.5) -a . -r requirements-dev.txt cbeams'

popve: ## Populate the active virtualenv
	pip install -r requirements-dev.txt


# development

test: ## Run tests
	py.test -q
.PHONY: test

lint: ## Run lint tools
	pylint *.py
.PHONY: lint

tags: ## Create tags
	ctags -R --languages=python .
.PHONY: tags

clean: ## Delete all temporary files, like *.pyc or __pycache__
	rm -rf build dist MANIFEST tags *.egg-info *.spec
	find . -name __pycache__ -type d | xargs rm -rf
.PHONY: clean

develop: ## Install this package in develop mode, so we can edit it
	@# i.e creates executable entry points in our python or virtualenv's bin dir
	@# Alternative implementation would be "python setup.py develop"
	pip install -e .
.PHONY: develop


# push to PyPI

sdist: ## Upload an sdist to PyPI
	python setup.py sdist --formats=gztar
.PHONY: sdist

# Pure Python wheel (since source does not support Python2)
wheel: ## Upload a wheel to PyPI
	python setup.py bdist_wheel
.PHONY: wheel

register: ## Update package metadata & docs on PyPI
	python setup.py register
.PHONY: register

upload: clean sdist wheel ## Not sure what this does, TBH
	twine upload dist/*
.PHONY: upload


# build a redistributable binary
# TODO: Put this in a script.
# TODO: Hardcoded program version

exe: clean ## Build a redistributable binary for the current platform
	bin/make-exe

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


help:
	@# Optionally add 'sort' before 'awk'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'
.PHONY: help

.DEFAULT_GOAL := help

