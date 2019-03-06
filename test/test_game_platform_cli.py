#!/usr/bin/env python3

from game_platform.game_platform import GamePlatform
from unittest import TestCase


class TestGamePlatformCLI(TestCase):
    """
    Tests the GamePlatform class CLI
    Author(s): Adam Ross
    Last-edit-date: 05/03/2019
    """

    def test_game_platform_class(self):
        """
        Tests GamePlatform class instance
        """
        test = GamePlatform()
        self.assertTrue(isinstance(test, GamePlatform))

    def test_display_game_pieces_at_game_start(self):
        """
        Tests displaying of piece pool at game initialization
        """
        test = GamePlatform()
        test.display.display_piece_pool()

    def test_display_game_pieces_at_first_selection(self):
        """
        Tests displaying of piece pool after first piece selected
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.selected_piece = '0000'
        test.display.display_piece_pool()

    def test_display_game_pieces_at_first_placement(self):
        """
        Tests displaying of pieces after first selected piece placed on board
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.selected_piece = '0000'
        test.play.game.board[0][0] = test.play.selected_piece
        test.display.display_piece_pool()

    def test_display_game_pieces_at_second_selection(self):
        """
        Tests displaying of piece pool after second piece selected
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.selected_piece = '1011'
        test.play.game.board[0][0] = '0'
        test.display.display_piece_pool()

    def test_display_game_pieces_at_second_placement(self):
        """
        Tests displaying of pieces after second selected piece placed on board
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.selected_piece = '1011'
        test.play.game.board[0][0] = '0'
        test.play.game.board[1][3] = test.play.selected_piece
        test.display.display_piece_pool()

    def test_display_game_pieces_at_third_selection(self):
        """
        Tests displaying of piece pool after third piece selected
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.game.pieces.pop('3')
        test.play.selected_piece = '0011'
        test.play.game.board[1][3] = '1011'
        test.play.game.board[0][0] = '0'
        test.display.display_piece_pool()

    def test_display_game_pieces_at_third_placement(self):
        """
        Tests displaying of pieces after third selected piece placed on board
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.game.pieces.pop('3')
        test.play.selected_piece = '0011'
        test.play.game.board[1][3] = '1011'
        test.play.game.board[0][0] = '0'
        test.play.game.board[2][2] = test.play.selected_piece
        test.display.display_piece_pool()

    def test_display_game_pieces_at_fourth_selection(self):
        """
        Tests displaying of piece pool after fourth piece selected
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.game.pieces.pop('3')
        test.play.game.pieces.pop('8')
        test.play.selected_piece = '1000'
        test.play.game.board[1][3] = '1011'
        test.play.game.board[0][0] = '0'
        test.display.display_piece_pool()

    def test_display_game_pieces_at_fourth_placement(self):
        """
        Tests displaying of pieces after fourth selected piece placed on board
        """
        test = GamePlatform()
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.game.pieces.pop('3')
        test.play.game.pieces.pop('8')
        test.play.selected_piece = '1000'
        test.play.game.board[1][3] = '1011'
        test.play.game.board[0][0] = '0'
        test.play.game.board[2][2] = '0011'
        test.play.game.board[0][1] = test.play.selected_piece
        test.display.display_piece_pool()

    def test_game_header_easy_ai_vs_ai(self):
        """
        Tests displaying of game header when easy AI vs AI
        """
        test = GamePlatform()
        test.play.init_players(3, 1)
        test.display.display_piece_pool()

    def test_game_header_medium_ai_vs_ai(self):
        """
        Tests displaying of game header when medium AI vs AI
        """
        test = GamePlatform()
        test.play.init_players(3, 2)
        test.display.display_piece_pool()

    def test_game_header_hard_ai_vs_ai(self):
        """
        Tests displaying of game header when hard AI vs AI
        """
        test = GamePlatform()
        test.play.init_players(3, 3)
        test.display.display_piece_pool()

    def test_game_header_user_vs_easy_ai(self):
        """
        Tests displaying of game header when easy AI vs user
        """
        test = GamePlatform()
        test.play.init_players(2, 1)
        test.display.display_piece_pool()

    def test_game_header_user_vs_medium_ai(self):
        """
        Tests displaying of game header when medium AI vs user
        """
        test = GamePlatform()
        test.play.init_players(2, 2)
        test.display.display_piece_pool()

    def test_game_header_user_vs_hard_ai(self):
        """
        Tests displaying of game header when hard AI vs user
        """
        test = GamePlatform()
        test.play.init_players(2, 3)
        test.display.display_piece_pool()

    def test_game_header_user_vs_user_selecting(self):
        """
        Tests displaying of game header when user vs user and selecting a piece
        """
        test = GamePlatform()
        test.play.init_players(1, 0)
        test.display.display_piece_pool()

    def test_game_header_user_vs_user_placing(self):
        """
        Tests displaying of game header when user vs user and placing a piece
        """
        test = GamePlatform()
        test.play.init_players(1, 0)
        test.play.selected_piece = '0000'
        test.display.display_piece_pool()

    def test_game_display_at_user_vs_user_init(self):
        """
        Tests the game status display at game initialization for user vs user
        """
        test = GamePlatform()
        test.play.init_players(1, 0, "Henry", "Ford")
        test.display.display_piece_pool()

    def test_game_display_at_user_vs_user_first_turn(self):
        """
        Tests the game status display after first selection for user vs user
        """
        test = GamePlatform()
        test.play.init_players(1, 0, "Caesar", "Augustus")
        test.play.game.pieces.pop('0')
        test.play.selected_piece = '0000'
        test.display.display_piece_pool()
