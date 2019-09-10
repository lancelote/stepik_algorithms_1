test:
	PYTHONPATH=src python -m pytest tests

lint:
	python -m mypy src/module_* --ignore-missing-imports

install:
	python -m pip install -r requirements.txt

deps:
	pur -r requirements.txt
