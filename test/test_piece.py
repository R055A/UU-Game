#!/usr/bin/env python3

from unittest import TestCase
from game_platform_gui.piece import Piece
from game_platform.piece import Piece as PieceCLI
from tkinter import Canvas

SIZE = 600  # the height and width of the test GUI canvas


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
        self.assertTrue(test.x_pos == 17.5 and test.y_pos == 417.5)

        test = Piece(Canvas(height=SIZE, width=SIZE), '0000')
        self.assertTrue(test.x_pos == 17.5 and test.y_pos == 17.5)

        test = Piece(Canvas(height=SIZE, width=SIZE), '0101')
        self.assertTrue(test.x_pos == 117.5 and test.y_pos == 117.5)

        test = Piece(Canvas(height=SIZE, width=SIZE), '1111')
        self.assertTrue(test.x_pos == 117.5 and test.y_pos == 517.5)

    def test_piece_colour(self):
        """
        Tests the colour for piece image at initialization
        """
        test = Piece(Canvas(height=SIZE, width=SIZE), '0000')
        self.assertTrue(test.colour == 'gray1')

        test = Piece(Canvas(height=SIZE, width=SIZE), '1111')
        self.assertTrue(test.colour == 'red')

    # def test_piece_shape(self):
    #     """
    #     Tests the shape for piece image at initialization
    #     """
    #     test = Piece(Canvas(height=SIZE, width=SIZE), '0000')
    #     self.assertTrue(test.canvas.type(1) == 'rectangle')
    #     self.assertFalse(test.horizontal)
    #     self.assertFalse(test.vertical)
    #
    #     test = Piece(Canvas(height=SIZE, width=SIZE), '1111')
    #     self.assertTrue(test.canvas.type(1) == 'oval')
    #     self.assertTrue(test.canvas.type(2) == 'rectangle')
    #     self.assertTrue(test.canvas.type(3) == 'rectangle')
    #
    #     test = Piece(Canvas(height=SIZE, width=SIZE), '1011')
    #     self.assertTrue(test.canvas.type(1) == 'rectangle')
    #     self.assertTrue(test.canvas.type(2) == 'rectangle')
    #     self.assertTrue(test.canvas.type(3) == 'rectangle')
    #
    #     test = Piece(Canvas(height=SIZE, width=SIZE), '0100')
    #     self.assertTrue(test.canvas.type(1) == 'oval')
    #     self.assertFalse(test.horizontal)
    #     self.assertFalse(test.vertical)

    def test_piece_cli(self):
        """
        Tests the CLI Piece class
        """
        pce = PieceCLI('0000')
        test = [PieceCLI(bin(i)[2:].zfill(4)) for i in range(16)]
        self.assertTrue(isinstance(test[0], PieceCLI))
        self.assertEqual(test[0].get_chars(), pce.FALSE_COL + "abc" +
                         pce.END_COL)
        self.assertEqual(test[1].get_chars(), pce.TRUE_COL + "abc" +
                         pce.END_COL)
        self.assertEqual(test[2].get_chars(), pce.FALSE_COL + "abC" +
                         pce.END_COL)
        self.assertEqual(test[3].get_chars(), pce.TRUE_COL + "abC" +
                         pce.END_COL)
        self.assertEqual(test[4].get_chars(), pce.FALSE_COL + "aBc" +
                         pce.END_COL)
        self.assertEqual(test[5].get_chars(), pce.TRUE_COL + "aBc" +
                         pce.END_COL)
        self.assertEqual(test[6].get_chars(), pce.FALSE_COL + "aBC" +
                         pce.END_COL)
        self.assertEqual(test[7].get_chars(), pce.TRUE_COL + "aBC" +
                         pce.END_COL)
        self.assertEqual(test[8].get_chars(), pce.FALSE_COL + "Abc" +
                         pce.END_COL)
        self.assertEqual(test[9].get_chars(), pce.TRUE_COL + "Abc" +
                         pce.END_COL)
        self.assertEqual(test[10].get_chars(), pce.FALSE_COL + "AbC" +
                         pce.END_COL)
        self.assertEqual(test[11].get_chars(), pce.TRUE_COL + "AbC" +
                         pce.END_COL)
        self.assertEqual(test[12].get_chars(), pce.FALSE_COL + "ABc" +
                         pce.END_COL)
        self.assertEqual(test[13].get_chars(), pce.TRUE_COL + "ABc" +
                         pce.END_COL)
        self.assertEqual(test[14].get_chars(), pce.FALSE_COL + "ABC" +
                         pce.END_COL)
        self.assertEqual(test[15].get_chars(), pce.TRUE_COL + "ABC" +
                         pce.END_COL)
