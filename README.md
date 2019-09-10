# Tricko!
An open source app to manage turns adapted like a Gecko. In few words, what is Tricko? Tricko is like the gecko of the
tickets machine, because Tricko adapts to the necessities of those who take a ticket and to environment. Do you really
need a printed ticket? Althought Tricko doesn't work yet with printers, Tricko recommends to use the digital ticket to
save paper.

## Installation

Tricko has a `Makefile` to ease its installation and usage. As we haven't released the first version yet, you need to
follow the next instructions:
  
  - Download this repository or clone it (`git clone ...`).
  - In your terminal, move to where you download or clone Tricko.
  - Run `make all`. It will install the Tricko's dependencies, the ones indicated in the `requirements.txt` file
   (`pyyaml`, `kivy` and `kivy-garden`) and the one part of the Kivy Garden (`garden.qrcode`).
  - Then run `python app.py`.
  - Enjoy and test Tricko!
  
As soon as possible we want to find an easier way to install Kivy. If you have any suggestion, you can write an issue!

## Usage

Tricko is very easy. You just need to run it with `python app.py` where you have Tricko source files. Then you have the
three buttons to interact, that by default are *Send*, *Receipt* and *Information*. You can change it in the `config.yaml`
file. It is also the file in which you can change another data, as you can see in the next section.

### Configuration

In the configuration file, `config.yaml`, there are two main fields:

  - `app`, dedicated to the app settings.
    - `title`, title of the window.
    - `width`, width of the window.
    - `height`, height of the window.
  - `options`, dedicated to the buttons for the type of ticket.
    - `send` and `send_code`, one for the label and another for its respective code (e.g. **S** for *Send*).
    - `receipt` and `receipt_code`. Ídem.
    - `info` and `info_code`. Ídem.

## Contributing

TODO

## Acknowledgements

An idea of [Pablo Hinojosa Nava](https://github.com/pablohn26), developed by [Iván Hernández Cazorla](https://github.com/ivanhercaz).
The name, Tricko, was an idea of [Santamarcanda](https://github.com/Santamarcanda).

## License

[GNU General Public License v3.0](https://github.com/ivanhercaz/tricko/blob/master/LICENSE)