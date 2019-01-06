SHELL=/bin/bash
VERSION:=$(shell cat fifbucket/version.py | cut -d "'" -f2)
export PATH := ./bin:./venv/bin:$(PATH)
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf " \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# The tests are written in Python. Make a virtualenv to handle the dependencies.
venv: requirements.txt ## Create virtualenv
	@if [ -z $$PYTHON3 ]; then\
		PY3_MINOR_VER=`python3 --version 2>&1 | cut -d " " -f 2 | cut -d "." -f 2`;\
		if (( $$PY3_MINOR_VER < 5 )); then\
		echo "Couldn't find python3 in \$PATH that is >=3.5";\
		echo "Please install python3.5 or later or explicity define the python3 executable name with \$PYTHON3";\
			echo "Exiting here";\
			exit 1;\
		else\
		export PYTHON3="python3.$$PY3_MINOR_VER";\
		fi;\
	fi;\
	test -d venv || virtualenv --python=$$PYTHON3 venv;\
	pip install -r requirements.txt;\
	touch venv;\

pip-compile: venv ## Compile requirements.txt
	pip install pip-tools;\
	pip-compile --output-file requirements.txt requirements.in

clean: ## Clean workspace
	rm -fr venv

lint: venv ## Run flake8
	flake8 *.py */*.py

test: venv ## Run tests
	pytest tests --doctest-modules -v --cov fifbucket --cov-report term-missing --cov-report xml

coveralls: venv ## Run coveralls
	coveralls

autopep8: venv ## Run autopep8
	autopep8 -i *.py */*.py

dev-local: venv ## install package in virtualenv
	pip install -e . --no-deps

build: venv ## build package
	python setup.py sdist; \
	python setup.py bdist_wheel;

upload: build ## upload package
	twine upload dist/fifbucket-$(VERSION)-py2.py3-none-any.whl; \
	twine upload dist/fifbucket-$(VERSION).tar.gz
