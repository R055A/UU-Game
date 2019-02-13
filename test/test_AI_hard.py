import unittest

from game_engine.play import Play
from game_engine.player_hard_ai import PlayerHardAI
from game_engine.game import Game
from random import choice

class MyTestCase(unittest.TestCase):

    def test_player_ai_hard(self):
        """
        Tests PlayerHardAI class instance
        """
        test = PlayerHardAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerHardAI))

    def test_AI_hard(self):
        """
        Test for the AI in difficulty hard by checking the win ratio against itself in AIvsAI
        """
        average = 0
        error = 0
        for i in range(100):

            test = Play()
            test.players = [PlayerHardAI(test.game, "Player One"),
                            PlayerHardAI(test.game, "Player Two")]
            test.current_player = choice(test.players)
            result = test.play_auto()
            if result == "Player One":
                average += 1
            elif result == "Player Two":
                average -= 1
            elif result is None:
                average += 0
            else:
                error += 1

        self.assertTrue(-5 < average < 5)
        self.assertEqual(error, 0)


if __name__ == '__main__':
    unittest.main()
