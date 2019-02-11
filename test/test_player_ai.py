from unittest import TestCase
from game_engine.game import Game
from game_engine.player_ai import PlayerAI


class TestPlayerAIClass(TestCase):
    """
    Tests the PlayerAI class
    Author(s): Adam Ross
    Date: 11/02/19
    """

    def test_player_ai(self):
        """
        Tests PlayerAI class instance
        """
        test = PlayerAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerAI))
