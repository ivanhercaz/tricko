# coding: utf-8
"""
    Tricko! An open source app to manage turns adapted like a Gecko.

    An idea of Pablo Hinojosa Nava (pablohn26), developed by Iván Hernández Cazorla (Ivanhercaz)

    TODO:
        - Control panel with password
        - Possibility to add a logo
"""

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout

import yaml

# Configuration file (YAML format)
with open("config.yaml", "r") as configFile:
    config = yaml.load(configFile, Loader=yaml.BaseLoader)

# TODO: add instructions to how to use new colors
# TODO: make easier the system to choice the colors
color = {
    "base": [120 / 250, 144 / 250, 156 / 250, 1],  # black
    "text": [1, 1, 1, 1],  # white
    "qrBackground": (1, 1, 1, 0.01),
}

# Kivy configuration
Config.set("graphics", "resizable", False)
Config.write()


class TrickoApp(App):
    # Counter properties
    count = NumericProperty(0)
    countSend = NumericProperty(-1)
    countReceipt = NumericProperty(-1)
    countInfo = NumericProperty(-1)

    # Next number properties
    nextNumberSend = ObjectProperty("S0")
    nextNumberReceipt = ObjectProperty("R0")
    nextNumberInfo = ObjectProperty("I0")

    # Current number
    currentNumber = ObjectProperty("NaN")

    def clickSend(self):
        """
            Action when the "Send" button is clicked
        """

        # Sum 1 to the sum of all the tickets obtained
        self.count += 1
        # Update the label that shows the sum of all tickets obtained
        # self.counterLabel.text = str(self.count)
        # Sum 1 to the sum of the tickets to "Send"
        self.countSend += 1
        # Calculate the next number as from the current number to "Send"
        self.nextNumberSend = self.countSend + 1

        # Mix the code with the next number
        value = config["options"]["send_code"] + str(self.nextNumberSend)
        # Update the text of the "Send" label, the current number label and the data of the QR code

        self.nextNumberSend, self.currentNumber = (
            value,
            value
        )

    def clickReceipt(self):
        """
            Action when the "Receipt" button is clicked.
        """
        self.count += 1

        self.countReceipt += 1
        self.nextNumberReceipt = self.countReceipt + 1

        value = config["options"]["receipt_code"] + str(self.nextNumberReceipt)
        self.nextNumberReceipt, self.currentNumber = (
            value,
            value
        )

    def clickInfo(self):
        """
            Action when the "Information" button is clicked
        """
        self.count += 1

        self.countInfo += 1
        self.nextNumberInfo = self.countInfo + 1

        value = config["options"]["receipt_code"] + str(self.nextNumberInfo)
        self.nextNumberInfo, self.currentNumber = (
            value,
            value
        )

    def build(self):
        """
            Builder
        :return: layout
        """

        # Configuration
        self.config = config
        self.color = color

        return RootLayout()


class RootLayout(BoxLayout):
    pass


if __name__ == "__main__":
    # Set the width and height of the window
    Window.size = int(config["app"]["width"]), int(config["app"]["height"])

    # Set the background color of the window with the base color chosen
    Window.clearcolor = color["base"]

    app = TrickoApp()
    app.title = config["app"]["title"]

    app.run()
