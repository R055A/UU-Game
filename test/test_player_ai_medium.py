from unittest import TestCase
from game_engine.play import Play
from game_engine.game import Game
from game_engine.player_ai_medium import PlayerMediumAI
from random import choice


class TestPlayerAIMediumClass(TestCase):
    """
    Tests the PlayerMediumAI class
    Author(s): Adam Ross; Gustav From
    Date: 12/02/19
    """

    def test_player_ai_medium(self):
        """
        Tests PlayerMediumAI class instance
        """
        test = PlayerMediumAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerMediumAI))

    def test_player_ai_medium_play(self):
        """
        Tests average PlayerMediumAI player wins 50% +/- 10% in non-drawn games
        """
        p_one, p_two, count, wins = "Player One", "Player Two", 0, 0
        samples = 100  # the number of samples of won games in each test
        tests = 5  # the number of tests

        for i in range(tests):
            while count < samples:
                test = Play()
                test.players = [PlayerMediumAI(test.game, p_one),
                                PlayerMediumAI(test.game, p_two)]
                test.current_player = choice(test.players)

                if test.play_auto():
                    count += 1

                    if test.current_player.name == p_one:
                        wins += 1
            self.assertTrue((40 <= wins <= 60))
            count, wins = 0, 0
