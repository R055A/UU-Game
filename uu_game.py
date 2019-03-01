#!/usr/bin/env python3

from communication_platform.main import CommunicationPlatform


class UUGame:
    """
    Starts and closes the UU-Game application
    Author(s): Adam Ross
    Last-edit-date: 23/02/2019
    """

    def __init__(self):
        """
        Class constructor
        """
        self.comms = CommunicationPlatform()

    def start_game(self):
        """
        Starts the communication platform with game menu options
        """
        self.comms.start_comms()

    def close_game(self):
        """
        Closes the communication platform with message before exiting program
        """
        self.comms.close_comms()


if __name__ == "__main__":
    app = UUGame()
    app.start_game()
    app.close_game()
