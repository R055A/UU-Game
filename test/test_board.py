from unittest import TestCase
from game_platform_gui.board import Board
from tkinter import Canvas

SIZE = 800  # the height and width of the test GUI canvas


class TestBoard(TestCase):
    """
    Tests the Board class
    Author(s): Laurin Kerle
    Last-edit-date: 24/02/2019
    """

    def test_board_class(self):
        """
        Tests board class instance
        """
        test = Board(Canvas(height=SIZE, width=SIZE), 10, 10, 10)
        self.assertTrue(isinstance(test, Board))



