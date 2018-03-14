SHELL=/bin/bash
export PATH := ./bin:./venv/bin:$(PATH)

# The tests are written in Python. Make a virtualenv to handle the dependencies.
venv: requirements.txt
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

pip-compile: venv
	pip install pip-tools;\
	pip-compile --output-file requirements.txt requirements.in

clean:
	rm -fr venv

lint: venv
	flake8 *.py */*.py

autopep8: venv
	autopep8 -i *.py */*.py

dev-local: venv
	pip install -e . --no-deps

build: venv
	python setup.py sdist;\
	python setup.py bdist_wheel

upload: venv
	twine upload dist/*
