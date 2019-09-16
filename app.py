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
    config = yaml.load(configFile, Loader=yaml.SafeLoader)

# Kivy configuration
Config.set("graphics", "resizable", False)
Config.write()


class TrickoApp(App):
    # Counter properties
    count = NumericProperty(0)
    countOptionA = NumericProperty(-1)
    countOptionB = NumericProperty(-1)
    countOptionC = NumericProperty(-1)
    countOptionD = NumericProperty(-1)
    countOptionE = NumericProperty(-1)
    countOptionF = NumericProperty(-1)

    # Next number properties
    nextOptionA = ObjectProperty(str(config["options"]["option_a"]["code"]) + "0")
    nextOptionB = ObjectProperty(str(config["options"]["option_b"]["code"]) + "0")
    nextOptionC = ObjectProperty(str(config["options"]["option_c"]["code"]) + "0")
    nextOptionD = ObjectProperty(str(config["options"]["option_d"]["code"]) + "0")
    nextOptionE = ObjectProperty(str(config["options"]["option_e"]["code"]) + "0")
    nextOptionF = ObjectProperty(str(config["options"]["option_f"]["code"]) + "0")

    # Current number
    currentNumber = ObjectProperty("NaN")

    def click_option_a(self):
        """
            Action when the "Send" button is clicked
        """

        # Sum 1 to the sum of all the tickets obtained
        self.count += 1
        # Update the label that shows the sum of all tickets obtained
        # self.counterLabel.text = str(self.count)
        # Sum 1 to the sum of the tickets to "Send"
        self.countOptionA += 1
        # Calculate the next number as from the current number to "Send"
        self.nextOptionA = self.countOptionA + 1

        # Mix the code with the next number
        value = self.options["option_a"]["code"] + str(self.nextOptionA)
        # Update the text of the "Send" label, the current number label and the data of the QR code

        self.nextOptionA, self.currentNumber = (
            value,
            value
        )

    def click_option_b(self):
        """
            Action when the "Receipt" button is clicked.
        """
        self.count += 1

        self.countOptionB += 1
        self.nextOptionB = self.countOptionB + 1

        value = self.options["option_b"]["code"] + str(self.nextOptionB)
        self.nextOptionB, self.currentNumber = (
            value,
            value
        )

    def click_option_c(self):
        """
            Action when the "Information" button is clicked
        """
        self.count += 1

        self.countOptionC += 1
        self.nextOptionC = self.countOptionC + 1

        value = self.options["option_c"]["code"] + str(self.nextOptionC)
        self.nextOptionC, self.currentNumber = (
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
        self.color = self.config["app"]["color"]
        self.numberOfOptions = self.config["app"]["options"]
        self.options = self.config["options"]

        if self.numberOfOptions is 2:
            return TwoOptionsLayout()
        elif self.numberOfOptions is 3:
            return ThreeOptionsLayout()
        elif self.numberOfOptions is 4:
            return FourOptionsLayout()
        elif self.numberOfOptions is 5:
            return FiveOptionsLayout()
        elif self.numberOfOptions is 6:
            return SixOptionsLayout()


class TwoOptionsLayout(BoxLayout):
    pass


class ThreeOptionsLayout(BoxLayout):
    pass


class FourOptionsLayout(BoxLayout):
    pass


class FiveOptionsLayout(BoxLayout):
    pass


class SixOptionsLayout(BoxLayout):
    pass

if __name__ == "__main__":
    # Set the width and height of the window
    Window.size = config["app"]["width"], config["app"]["height"]

    Window.clearcolor = config["app"]["color"]["base"]

    app = TrickoApp()
    app.title = config["app"]["title"]

    app.run()
