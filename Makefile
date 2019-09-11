.DEFAULT: all

all: install-dependencies install-garden-dependencies
	@echo "test"

install-dependencies:
	pip -r requirements.txt

install-garden-dependencies:
	garden install garden.qrcode --app

global:
	chmod +x tricko
	cp tricko.sh tricko
	sed -i "s+app.py+$(PWD)/app.py+g" tricko
	sudo cp tricko /usr/local/bin
