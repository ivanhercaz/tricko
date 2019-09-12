# coding: utf-8
"""
    Tricko! An open source app to manage turns adapted like a Gecko.

    An idea of Pablo Hinojosa Nava (pablohn26), developed by Iván Hernández Cazorla (Ivanhercaz)

    TODO:
        - Control panel with password
        - Possibility to add a logo
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config

from kivy.properties import ListProperty
from kivy.properties import NumericProperty

from kivy.garden.qrcode import QRCodeWidget

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
    count = NumericProperty()
    countSend = NumericProperty()
    countReceipt = NumericProperty()
    countInfo = NumericProperty()

    # Next number properties
    nextNumberSend = NumericProperty()
    nextNumberReceipt = NumericProperty()
    nextNumberInfo = NumericProperty()

    def clickSend(self):
        """
            Action when the "Send" button is clicked
        """

        # Sum 1 to the sum of all the tickets obtained
        self.count += 1
        # Update the label that shows the sum of all tickets obtained
        self.counterLabel.text = str(self.count)
        # Sum 1 to the sum of the tickets to "Send"
        self.countSend += 1
        # Calculate the next number as from the current number to "Send"
        self.nextNumberSend = self.countSend + 1

        # Mix the code with the next number
        value = config["options"]["send_code"] + str(self.nextNumberSend)
        # Update the text of the "Send" label, the current number label and the data of the QR code
        self.nextNumberSendLabel.text, self.currentNumberLabel.text, self.currentNumberQR.data = (
            value,
            value,
            value,
        )

    def clickReceipt(self):
        """
            Action when the "Receipt" button is clicked.
        """
        self.count += 1
        self.counterLabel.text = str(self.count)

        self.countReceipt += 1
        self.nextNumberReceipt = self.countReceipt + 1

        value = config["options"]["receipt_code"] + str(self.nextNumberReceipt)
        self.nextNumberReceiptLabel.text, self.currentNumberLabel.text, self.currentNumberQR.data = (
            value,
            value,
            value,
        )

    def clickInfo(self):
        """
            Action when the "Information" button is clicked
        """
        self.count += 1
        self.counterLabel.text = str(self.count)

        self.countInfo += 1
        self.nextNumberInfo = self.countInfo + 1

        value = config["options"]["info_code"] + str(self.nextNumberInfo)
        self.nextNumberInfoLabel.text, self.currentNumberLabel.text, self.currentNumberQR.data = (
            value,
            value,
            value,
        )

    def build(self):
        """
            Builder
        :return: layout
        """

        # Main layout (BoxLayout)
        """
        layout = RootLayout()
        layout.orientation = "horizontal"
        """
        # Configuration
        self.config = config
        self.color = color

        self.count = 0
        self.countSend, self.countReceipt, self.countInfo = -1, -1, -1
        self.nextNumberSend, self.nextNumberReceipt, self.nextNumberInfo = 0, 0, 0

        return RootLayout()

        """
        self.nextNumberSend, self.nextNumberReceipt, self.nextNumberInfo = 0, 0, 0

        self.nextNumberSendLabel = Label(
            text=config["options"]["send_code"] + str(self.nextNumberSend),
            font_size=50,
            color=color["text"],
        )
        self.nextNumberSendLabel.size_hint = 1, 1.75

        self.nextNumberReceiptLabel = Label(
            text=config["options"]["receipt_code"] + str(self.nextNumberReceipt),
            font_size=50,
            color=color["text"],
        )
        self.nextNumberReceiptLabel.size_hint = 1, 1.75

        self.nextNumberInfoLabel = Label(
            text=config["options"]["info_code"] + str(self.nextNumberInfo),
            font_size=50,
            color=color["text"],
        )
        self.nextNumberInfoLabel.size_hint = 1, 1.75

        # Buttons for each action
        buttonSend.on_press = self.clickSend

        buttonReceipt.on_press = self.clickReceipt

        buttonInfo.on_press = self.clickInfo

        # Sublayout (left column) to group items
        verticalLayout = BoxLayout()
        verticalLayout.orientation = "vertical"

        # Items of the sublayout (left column)
        verticalLayout.add_widget(Label(text="Number of tickets distributed"))
        verticalLayout.add_widget(self.counterLabel)
        verticalLayout.add_widget(buttonSend)
        verticalLayout.add_widget(buttonReceipt)
        verticalLayout.add_widget(buttonInfo)
        verticalLayout.add_widget(Label(text="Next number"))

        # Sublayout (next numbers) to group the next numbers set
        horizontalLayout = BoxLayout()
        horizontalLayout.orientation = "horizontal"

        # Items of the sublayout (next numbers)
        horizontalLayout.add_widget(self.nextNumberSendLabel)
        horizontalLayout.add_widget(self.nextNumberReceiptLabel)
        horizontalLayout.add_widget(self.nextNumberInfoLabel)

        # Insert the next numbers layout to the vertical left column layout
        verticalLayout.add_widget(horizontalLayout)

        # Sublayout (right column) to group items
        verticalRightLayout = BoxLayout()
        verticalRightLayout.orientation = "vertical"

        # Current number (the last one obtained) and its label
        self.currentNumber = "NaN"
        self.currentNumberLabel = Label(
            text=self.currentNumber,
            font_size=50,
            color=color["text"],
            size_hint=(1, 0.5),
        )

        """
        """
            QR code generated with the current number as data (eg. E5)
            
            TODO: the data should be something more specific than a string with the number, like a link to an app or a
                website to have digitally the QR and the number to show to the operator.
        """
        """
        self.currentNumberQR = QRCodeWidget(
            id="qrNumber",
            data=self.currentNumberLabel.text,
            show_border=False,
            background_color=color["qrBackground"],
        )

        # Items of the sublayout (right column)
        verticalRightLayout.add_widget(Label(text="Your number is", size_hint=(1, 0.5)))
        verticalRightLayout.add_widget(self.currentNumberLabel)
        verticalRightLayout.add_widget(self.currentNumberQR)
        verticalRightLayout.add_widget(
            Label(
                text="Scan this QR code or take a photograph of it", size_hint=(1, 0.7)
            )
        )

        # Insert left and right columns in the main layout
        layout.add_widget(verticalLayout)
        layout.add_widget(verticalRightLayout)

        return layout
        """

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
