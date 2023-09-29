all: plot.pdf


plot.pdf: plot_sine.py
	python plot_sine.py

clean:
	rm -f plot.pdf


.PHONY: all clean
