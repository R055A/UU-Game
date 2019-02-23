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
        test.quit()
        test.destroy()

    def test_pieces_created(self):
        """
        Tests sixteen unique game piece created at initialization
        """
        test = GamePlatform(Tk(), Play())
        self.assertTrue(len(test.pieces) == 16 and len(test.pieces) * 2
                        == len(test.canvas.find_all()))
        self.assertTrue(test.pieces[i].colour == 'red' and test.canvas.type(i)
                        == 'rectangle' for i in range(8))
        self.assertTrue(test.pieces[i].colour == 'gray1' for i in range(8, 16))
        self.assertTrue(test.canvas.type(9) == 'oval')
        self.assertTrue(test.canvas.type(10) == 'oval')
        self.assertTrue(test.canvas.type(11) == 'rectangle')
        self.assertTrue(test.canvas.type(12) == 'oval')
        self.assertTrue(test.canvas.type(13) == 'rectangle')
        self.assertTrue(test.canvas.type(14) == 'oval')
        self.assertTrue(test.canvas.type(15) == 'rectangle')
        self.assertTrue(test.canvas.type(16) == 'rectangle')
        self.assertTrue(test.canvas.type(i) == 'rectangle' for i in range(16, 24))
        self.assertTrue(test.canvas.type(25) == 'oval')
        self.assertTrue(test.canvas.type(26) == 'oval')
        self.assertTrue(test.canvas.type(27) == 'rectangle')
        self.assertTrue(test.canvas.type(28) == 'oval')
        self.assertTrue(test.canvas.type(29) == 'rectangle')
        self.assertTrue(test.canvas.type(30) == 'oval')
        self.assertTrue(test.canvas.type(31) == 'rectangle')
        self.assertTrue(test.canvas.type(32) == 'rectangle')
