#!/usr/bin/env python3

from game_platform.piece import Piece as PieceCLI
from unittest import TestCase


class TestGamePlatformCLI(TestCase):
    """
    Tests the GamePlatform class CLI
    Author(s): Adam Ross
    Last-edit-date: 22/03/2019
    """

    def test_piece_class(self):
        """
        Tests GamePlatform class instance
        """
        test = PieceCLI('0000')
        self.assertTrue(isinstance(test, PieceCLI))

    def test_piece_cli(self):
        """
        Tests the CLI Piece class
        """
        pce = PieceCLI('0000')  # temporary for colouring pieces
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
