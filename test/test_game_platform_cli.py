from game_platform.game_platform import GamePlatform
from game_engine.play import Play
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
        test = GamePlatform(Play())
        self.assertTrue(isinstance(test, GamePlatform))

    def test_display_game_pieces_at_game_start(self):
        """
        Tests displaying of piece pool at game initialization
        """
        test = GamePlatform(Play())
        test.display_piece_pool()

    def test_display_game_pieces_at_first_selection(self):
        """
        Tests displaying of piece pool after first piece selected
        """
        test = GamePlatform(Play())
        test.play.game.pieces.pop('0')
        test.play.selected_piece = '0000'
        test.display_piece_pool()

    def test_display_game_pieces_at_first_placement(self):
        """
        Tests displaying of pieces after first selected piece placed on board
        """
        test = GamePlatform(Play())
        test.play.game.pieces.pop('0')
        test.play.selected_piece = '0000'
        test.play.game.board[0][0] = test.play.selected_piece
        test.display_piece_pool()

    def test_display_game_pieces_at_second_selection(self):
        """
        Tests displaying of piece pool after second piece selected
        """
        test = GamePlatform(Play())
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.selected_piece = '1011'
        test.play.game.board[0][0] = '0'
        test.display_piece_pool()

    def test_display_game_pieces_at_second_placement(self):
        """
        Tests displaying of pieces after second selected piece placed on board
        """
        test = GamePlatform(Play())
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.selected_piece = '1011'
        test.play.game.board[0][0] = '0'
        test.play.game.board[1][3] = test.play.selected_piece
        test.display_piece_pool()

    def test_display_game_pieces_at_third_selection(self):
        """
        Tests displaying of piece pool after third piece selected
        """
        test = GamePlatform(Play())
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.game.pieces.pop('3')
        test.play.selected_piece = '0011'
        test.play.game.board[1][3] = '1011'
        test.play.game.board[0][0] = '0'
        test.display_piece_pool()

    def test_display_game_pieces_at_third_placement(self):
        """
        Tests displaying of pieces after third selected piece placed on board
        """
        test = GamePlatform(Play())
        test.play.game.pieces.pop('0')
        test.play.game.pieces.pop('11')
        test.play.game.pieces.pop('3')
        test.play.selected_piece = '0011'
        test.play.game.board[1][3] = '1011'
        test.play.game.board[0][0] = '0'
        test.play.game.board[2][2] = test.play.selected_piece
        test.display_piece_pool()
