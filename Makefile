.DEFAULT: all

all: install-dependencies install-garden-dependencies
	@echo "test"

install-dependencies:
	pip install pyyaml
	python -m pip install kivy
	pip install qrcode

install-garden-dependencies:
	pip install kivy-garden
	garden install garden.qrcode --app
