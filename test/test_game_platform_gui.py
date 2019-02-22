from unittest import TestCase
from game_platform.game_platform import GamePlatform
from game_engine.play import Play
from tkinter import Tk
from time import sleep


class TestGamePlatform(TestCase):
    """
    Tests the GamePlatform class GUI
    Author(s): Adam Ross
    Last-edit-date: 22/02/2019
    """

    def test_game_platform_class(self):
        """
        Tests GamePlatform class instance
        """
        test = GamePlatform(Tk(), Play())
        self.assertTrue(isinstance(test, GamePlatform))
        test.update()
        sleep(15)
        test.destroy()
