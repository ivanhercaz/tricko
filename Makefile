.DEFAULT: all

all: install-dependencies install-garden-dependencies
	@echo "test"

install-dependencies:
	pip -r requirements.txt

install-garden-dependencies:
	garden install garden.qrcode --app
