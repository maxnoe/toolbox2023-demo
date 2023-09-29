all: build/plot.pdf


build/plot.pdf: plot_sine.py | build
	python plot_sine.py


build:
	mkdir -p build

clean:
	rm -rf build


.PHONY: all clean
