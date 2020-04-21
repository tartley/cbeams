# This Makefile is just a cheatsheet to remind me of some commonly used
# commands. I'm generally executing these on Ubuntu, but have in the past
# used them on OSX with up-to-date gnu binaries, or WindowsXP/7 with Cygwin
# binaries foremost on the PATH.

PROJ=cbeams
PYVERSION=python3.8
VENV=$(HOME)/.virtualenvs/$(PROJ)
BIN=$(VENV)/bin

# help

help: ## Show this help.
	@# Optionally add 'sort' before 'awk'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'
.PHONY: help


# virtualenv

venv: ## Create the virtualenv, or clear installed packages from it.
	# Use system python for this. Other steps will use venv's symlink to it.
	$(PYVERSION) -m venv $(VENV) --clear
.PHONY: venv

popve: ## Populate the virtualenv.
	$(BIN)/pip install -U -r requirements-dev.txt
.PHONY: popve

bootstrap: venv popve ## Set up a development environment.
.PHONY: bootstrap

develop: ## Install this package in develop mode, so we can edit it
	@# i.e creates executable entry points in our python or virtualenv's bin dir
	@# Alternative implementation would be "python setup.py develop"
	pip install -e .
.PHONY: develop


# development

test: ## Run tests
	$(BIN)/pytest -q
.PHONY: test

lint: ## Run lint tools
	$(BIN)/pylint *.py
.PHONY: lint

tags: ## Create tags
	ctags -R --languages=python .
.PHONY: tags

clean: ## Delete all temporary files
	rm -rf build dist MANIFEST tags *.egg-info *.spec
	find . -name __pycache__ -type d | xargs rm -rf
.PHONY: clean


# push to PyPI

# Hence normal releases will just be: make upload

dist: ## Create an sdist and a wheel
	$(BIN)/python setup.py sdist --formats=gztar bdist_wheel
.PHONY: dist

register: ## Create the package on PyPI, with docs.
	$(BIN)/python setup.py register
.PHONY: register

upload-test: clean dist ## Upload sdist and wheel to TEST PyPI
	$(BIN)/twine upload -r testpypi dist/*.whl dist/*.gz
.PHONY: upload

upload: clean dist ## Upload sdist and wheel to PyPI
	$(BIN)/twine upload dist/*whl dist/*gz
.PHONY: upload

