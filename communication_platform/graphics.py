#!/usr/bin/env python3

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[31m'
END_TC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


class Graphics:
    """
    A class to hold shorthands for different color formats
    Refactoring/integration editor(s): Adam Ross
    Last-edit-date: 24/02/2019
    """

    def __init__(self):
        """
        Class constructor
        """
        self.text = None

    def make_header(self, title):
        """
        Formats a given string as a graphical header
        :param title: string input that must be < 48 chars long
        """
        header, width, length, self.text, colour = "", 50, 9, title, "P"

        if len(self.text) % 2 == 0:
            difference = int(24 - (len(self.text) / 2))
        else:
            difference = int(24 - ((len(self.text) - 1) / 2))
        self.text = self.set_color(colour)

        for i in range(width):
            header += "-"
        header += "\n|"

        for i in range(difference):
            header += " "
        header += self.text

        while len(header) < width * 2 + length:
            header += " "
        header += "|\n"

        for i in range(width):
            header += "-"
        print(header)

    def set_color(self, colour, text=None):
        """
        Adds colour to a string header indicated by variable color
        :param colour: the colour the text is being set to
        :param text: the text being coloured
        :return: the coloured text
        """
        if text:
            self.text = text

        if colour == "G":
            return GREEN + self.text + END_TC
        elif colour == "Y":
            return YELLOW + self.text + END_TC
        elif colour == "P":
            return PURPLE + self.text + END_TC
        elif colour == "R":
            return RED + self.text + END_TC
        else:
            return self.text
