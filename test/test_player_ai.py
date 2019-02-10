from unittest import TestCase
from game_engine.play import Play
from game_engine.game import Game
from game_engine.player_ai import PlayerAI
from game_engine.player_ai_medium import PlayerMediumAI
from random import choice


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

    def test_medium_ai_vs_medium_ai(self):
        """
        Tests medium AI vs medium AI 100 times to averages wins to check if 50%
        """
        count, wins, total = 0, 0, 0

        while count < 100:
            test = Play()
            test.players = [PlayerMediumAI(test.game, "Player One"), PlayerMediumAI(test.game, "Player Two")]
            test.current_player = choice(test.players)
            winner = test.play_auto()

            if winner:
                count += 1

                if winner == "Player One":
                    wins += 1
            total += 1
        print(str(wins) + " ; " + str(total))
