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
        Tests PlayerMediumAI game play average player one wins 50% +/- 10%
        """
        p_one, p_two, count, wins = "Player One", "Player Two", 0, 0

        for i in range(100):
            while count < 100:
                test = Play()
                test.players = [PlayerMediumAI(test.game, p_one),
                                PlayerMediumAI(test.game, p_two)]
                test.current_player = choice(test.players)  # random starting player

                while True:
                    test.play_selection()
                    test.play_placement()

                    if test.game.has_won_game():  # checks if game won
                        count += 1

                        if test.current_player.name == p_one:
                            wins += 1
                        break
                    elif not test.game.has_next_play():  # checks if play turns remaining
                        break
            self.assertTrue((40 <= wins <= 60))
