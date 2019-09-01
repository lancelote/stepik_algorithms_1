test:
	PYTHONPATH=python/src python -m pytest python/tests

lint:
	python -m mypy python/src/module_* --ignore-missing-imports
	cargo check --manifest-path=rust/Cargo.toml

install:
	python -m pip install -r requirements.txt

deps:
	pur -r requirements.txt