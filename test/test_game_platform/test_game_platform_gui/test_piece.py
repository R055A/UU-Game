#!/usr/bin/env python3

from unittest import TestCase
from game_platform.game_platform_gui.piece import Piece
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
