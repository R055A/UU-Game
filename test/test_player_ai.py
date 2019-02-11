from unittest import TestCase
from game_engine.game import Game
from game_engine.player_ai import PlayerAI


class TestPlayerAIClass(TestCase):
    """
    Tests the PlayerAI class
    Author(s): Adam Ross
    Date: 10/02/19
    """

    def test_player_ai(self):
        """
        Tests PlayerAI class instance
        """
        test = PlayerAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerAI))
        test.game.board = [['0001', '1000', '0000', '0011'],
                      [None, None, None, None],
                      [None, None, None, None],
                      [None, None, None, None]]
        test.hard('0000')
