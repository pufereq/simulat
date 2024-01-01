all:
	@echo "make run   - launch simulat"
	@echo "make venv  - create virtual environment"
	@echo "make clean - remove virtual environment and pyc files"

.PHONY: run
run: venv
	. venv/bin/activate; python3 simulat.py

venv:
	python3 -m venv venv/
	. venv/bin/activate; python3 -m pip install --upgrade pip
	. venv/bin/activate; python3 -m pip install -Ur requirements.txt

.PHONY: clean
clean:
	rm -rf venv/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete