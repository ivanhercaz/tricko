.DEFAULT: all

all: install-dependencies install-garden-dependencies
	@echo "test"

install-dependencies:
	pip install pyyaml
	python -m pip install kivy
	pip install qrcode

install-garden-dependencies:
	wget https://raw.githubusercontent.com/kivy-garden/garden.qrcode/master/__init__.py -P gardenqrcode
