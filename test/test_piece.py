from unittest import TestCase
from game_platform.piece import Piece
from tkinter import Canvas

SIZE = 600  # the height and width of the test GUI canvas


class TestPiece(TestCase):
    """
    Tests the Piece class
    Author(s): Adam Ross
    Last-edit-date: 22/02/2019
    """

    def test_piece_class(self):
        """
        Tests Piece class instance
        """
        test = Piece(Canvas(height=SIZE, width=SIZE), '1010')
        self.assertTrue(isinstance(test, Piece))

    def test_piece_coords(self):
        """
        Tests the x and y coords for a piece image at initialization
        """
        test = Piece(Canvas(height=SIZE, width=SIZE), '1010')
        self.assertTrue(test.x_pos == 15 and test.y_pos == 415)

        test = Piece(Canvas(height=SIZE, width=SIZE), '0000')
        self.assertTrue(test.x_pos == 15 and test.y_pos == 15)

        test = Piece(Canvas(height=SIZE, width=SIZE), '0101')
        self.assertTrue(test.x_pos == 115 and test.y_pos == 115)

        test = Piece(Canvas(height=SIZE, width=SIZE), '1111')
        self.assertTrue(test.x_pos == 115 and test.y_pos == 515)

    def test_piece_colour(self):
        """
        Tests the colour for piece image at initialization
        """
        test = Piece(Canvas(height=SIZE, width=SIZE), '0000')
        self.assertTrue(test.colour == 'gray1')

        test = Piece(Canvas(height=SIZE, width=SIZE), '1111')
        self.assertTrue(test.colour == 'red')
