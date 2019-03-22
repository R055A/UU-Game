#!/usr/bin/env python3

from game_platform.game_platform import GamePlatform
from unittest import TestCase, mock


class TestGamePlatformCLI(TestCase):
    """
    Tests the GamePlatform class
    Author(s): Adam Ross
    Last-edit-date: 22/03/2019
    """

    def test_game_platform_class(self):
        """
        Tests GamePlatform class instance
        """
        test = GamePlatform("")
        self.assertTrue(isinstance(test, GamePlatform))

    def test_place_piece_user(self):
        """
        Tests the place_piece method for when user player
        """
        test = GamePlatform("")
        test.play.init_players({"Caesar": [True, 0], "Augustus": [True, 0]})
        test.play.selected_piece = '0000'
        with mock.patch('builtins.input', return_value="1"):
            test.place_piece()
        self.assertEqual(test.play.game.board[0][0], '0000')

    def test_place_piece_AI(self):
        """
        Tests the place_piece method for when AI player
        """
        test = GamePlatform("")
        test.play.init_players({"Caesar": [False, 1], "Augustus": [False, 2]})
        test.play.selected_piece = '0000'
        test.place_piece()
        self.assertEqual([test.play.game.board[i][j] for j in range(4) for i in
                          range(4) if test.play.game.board[i][j]][0], '0000')

    def test_select_piece_user(self):
        """
        Tests the select_piece method for when user player
        """
        test = GamePlatform("")
        test.play.init_players({"Caesar": [True, 0], "Augustus": [True, 0]})
        with mock.patch('builtins.input', return_value="1"):
            test.select_piece()
        self.assertEqual(test.play.selected_piece, '0000')

    def test_select_piece_AI(self):
        """
        Tests the select_piece method for when AI player
        """
        test = GamePlatform("")
        test.play.init_players({"Caesar": [False, 1], "Augustus": [False, 2]})
        temp = test.play.game.pieces.copy()
        test.select_piece()
        [temp.pop(k) for k in test.play.game.pieces.keys()]
        self.assertTrue(list(temp)[0], test.play.selected_piece)

    def test_play_local_automated(self):
        """
        Tests the play_local method when AI vs AI
        """
        test = GamePlatform("")
        test.play.init_players({"Caesar": [False, 1], "Augustus": [False, 2]})
        self.assertTrue(test.play_local(True) in ["Caesar", "Augustus"])
