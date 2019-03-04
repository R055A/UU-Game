from unittest import TestCase
from game_platform_gui.game_platform import GamePlatform
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
        sleep(2)
        test.quit()
        test.destroy()

    # def test_pieces_created(self):
    #     """
    #     Tests sixteen unique game piece created at initialization
    #     """
    #     test = GamePlatform(Tk(), Play())
    #     self.assertTrue(len(test.pieces) == 16 and len(test.pieces) * 2
    #                     <= len(test.canvas.find_all()))
    #     self.assertTrue(test.pieces[i].colour == 'red' for i in range(8))
    #     self.assertTrue(test.pieces[i].colour == 'gray1' for i in range(8, 16))
    #     self.assertTrue(test.canvas.type(1) == 'rectangle')
    #     self.assertTrue(test.canvas.type(2) == 'text')
    #     self.assertTrue(test.canvas.type(3) == 'rectangle')
    #     self.assertTrue(test.canvas.type(4) == 'rectangle')
    #     self.assertTrue(test.canvas.type(5) == 'text')
    #     self.assertTrue(test.canvas.type(6) == 'rectangle')
    #     self.assertTrue(test.canvas.type(7) == 'rectangle')
    #     self.assertTrue(test.canvas.type(8) == 'text')
    #     self.assertTrue(test.canvas.type(9) == 'rectangle')
    #     self.assertTrue(test.canvas.type(10) == 'rectangle')
    #     self.assertTrue(test.canvas.type(11) == 'rectangle')
    #     self.assertTrue(test.canvas.type(12) == 'text')
    #     self.assertTrue(test.canvas.type(13) == 'oval')
    #     self.assertTrue(test.canvas.type(14) == 'text')
    #     self.assertTrue(test.canvas.type(15) == 'oval')
    #     self.assertTrue(test.canvas.type(16) == 'rectangle')
    #     self.assertTrue(test.canvas.type(17) == 'text')
    #     self.assertTrue(test.canvas.type(18) == 'oval')
    #     self.assertTrue(test.canvas.type(19) == 'rectangle')
    #     self.assertTrue(test.canvas.type(20) == 'text')
    #     self.assertTrue(test.canvas.type(21) == 'oval')
    #     self.assertTrue(test.canvas.type(22) == 'rectangle')
    #     self.assertTrue(test.canvas.type(23) == 'rectangle')
    #     self.assertTrue(test.canvas.type(24) == 'text')
    #     self.assertTrue(test.canvas.type(25) == 'rectangle')
    #     self.assertTrue(test.canvas.type(26) == 'text')
    #     self.assertTrue(test.canvas.type(27) == 'rectangle')
    #     self.assertTrue(test.canvas.type(28) == 'rectangle')
    #     self.assertTrue(test.canvas.type(29) == 'text')
    #     self.assertTrue(test.canvas.type(30) == 'rectangle')
    #     self.assertTrue(test.canvas.type(31) == 'rectangle')
    #     self.assertTrue(test.canvas.type(32) == 'text')
    #     self.assertTrue(test.canvas.type(33) == 'rectangle')
    #     self.assertTrue(test.canvas.type(34) == 'rectangle')
    #     self.assertTrue(test.canvas.type(35) == 'rectangle')
    #     self.assertTrue(test.canvas.type(36) == 'text')
    #     self.assertTrue(test.canvas.type(37) == 'oval')
    #     self.assertTrue(test.canvas.type(38) == 'text')
    #     self.assertTrue(test.canvas.type(39) == 'oval')
    #     self.assertTrue(test.canvas.type(40) == 'rectangle')
    #     self.assertTrue(test.canvas.type(41) == 'text')
    #     self.assertTrue(test.canvas.type(42) == 'oval')
    #     self.assertTrue(test.canvas.type(43) == 'rectangle')
    #     self.assertTrue(test.canvas.type(44) == 'text')
    #     self.assertTrue(test.canvas.type(45) == 'oval')
    #     self.assertTrue(test.canvas.type(46) == 'rectangle')
    #     self.assertTrue(test.canvas.type(47) == 'rectangle')
    #     self.assertTrue(test.canvas.type(48) == 'text')

    def test_move_selected_piece(self):
        """
        Tests the move_selected_piece() method in game_platform GUI class
        """
        test = GamePlatform(Tk(), Play())
        self.assertTrue(len(test.pieces) == 16 and len(test.pieces) * 2
                        <= len(test.canvas.find_all()))
        self.assertTrue(test.pieces['0'].x_pos == 17.5 and
                        test.pieces['0'].y_pos == 17.5)
        test.update()
        sleep(2)
        test.move_selected_piece(1)
        self.assertTrue(test.pieces['0'].x_pos == 500 and
                        test.pieces['0'].y_pos == 50)
        test.update()
        sleep(2)
        test.quit()
        test.destroy()
