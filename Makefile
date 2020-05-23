test:
	$(MAKE) -C python test
	$(MAKE) -C rust test

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