test:
	$(MAKE) -C test python
	$(MAKE) -C test rust

check:
	$(MAKE) -C python lint
	$(MAKE) -C rust check

install:
	$(MAKE) -C python install

deps:
	$(MAKE) -C python deps

clean:
	$(MAKE) -C rust clean

build:
	$(MAKE) -C rust build