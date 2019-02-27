from unittest import TestCase
from game_platform_gui.piece import Piece
from game_platform.piece import Piece as PieceCLI
from tkinter import Canvas

SIZE = 600  # the height and width of the test GUI canvas
TRUE_COL = '\033[94m'  # the fourth characteristic for each piece when true
FALSE_COL = '\033[93m'  # the fourth characteristic for each piece when false
END_COL = '\033[0m'  # to reset back to normal text colour


class TestPiece(TestCase):
    """
    Tests the Piece class
    Author(s): Adam Ross
    Last-edit-date: 27/02/2019
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

    def test_piece_shape(self):
        """
        Tests the shape for piece image at initialization
        """
        test = Piece(Canvas(height=SIZE, width=SIZE), '0000')
        self.assertTrue(test.canvas.type(1) == 'rectangle')
        self.assertFalse(test.horizontal)
        self.assertFalse(test.vertical)

        test = Piece(Canvas(height=SIZE, width=SIZE), '1111')
        self.assertTrue(test.canvas.type(1) == 'oval')
        self.assertTrue(test.canvas.type(2) == 'rectangle')
        self.assertTrue(test.canvas.type(3) == 'rectangle')

        test = Piece(Canvas(height=SIZE, width=SIZE), '1011')
        self.assertTrue(test.canvas.type(1) == 'rectangle')
        self.assertTrue(test.canvas.type(2) == 'rectangle')
        self.assertTrue(test.canvas.type(3) == 'rectangle')

        test = Piece(Canvas(height=SIZE, width=SIZE), '0100')
        self.assertTrue(test.canvas.type(1) == 'oval')
        self.assertFalse(test.horizontal)
        self.assertFalse(test.vertical)

    def test_piece_cli(self):
        """
        Tests the CLI Piece class
        """
        test = [PieceCLI(bin(i)[2:].zfill(4)) for i in range(16)]
        self.assertTrue(isinstance(test[0], PieceCLI))
        self.assertEqual(test[0].get_chars(), FALSE_COL + "abc" + END_COL)
        self.assertEqual(test[1].get_chars(), TRUE_COL + "abc" + END_COL)
        self.assertEqual(test[2].get_chars(), FALSE_COL + "abC" + END_COL)
        self.assertEqual(test[3].get_chars(), TRUE_COL + "abC" + END_COL)
        self.assertEqual(test[4].get_chars(), FALSE_COL + "aBc" + END_COL)
        self.assertEqual(test[5].get_chars(), TRUE_COL + "aBc" + END_COL)
        self.assertEqual(test[6].get_chars(), FALSE_COL + "aBC" + END_COL)
        self.assertEqual(test[7].get_chars(), TRUE_COL + "aBC" + END_COL)
        self.assertEqual(test[8].get_chars(), FALSE_COL + "Abc" + END_COL)
        self.assertEqual(test[9].get_chars(), TRUE_COL + "Abc" + END_COL)
        self.assertEqual(test[10].get_chars(), FALSE_COL + "AbC" + END_COL)
        self.assertEqual(test[11].get_chars(), TRUE_COL + "AbC" + END_COL)
        self.assertEqual(test[12].get_chars(), FALSE_COL + "ABc" + END_COL)
        self.assertEqual(test[13].get_chars(), TRUE_COL + "ABc" + END_COL)
        self.assertEqual(test[14].get_chars(), FALSE_COL + "ABC" + END_COL)
        self.assertEqual(test[15].get_chars(), TRUE_COL + "ABC" + END_COL)
