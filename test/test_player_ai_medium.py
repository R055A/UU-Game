from unittest import TestCase
from game_engine.play import Play
from game_engine.game import Game
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_easy_ai import PlayerEasyAI
from random import choice

from game_engine.player_hard_ai import PlayerHardAI


class TestPlayerAIMediumClass(TestCase):
    """
    Tests the PlayerMediumAI class
    Author(s): Adam Ross; Gustav From
    Date: 13/02/19
    """

    def test_player_ai_medium(self):
        """
        Tests PlayerMediumAI class instance
        """
        test = PlayerMediumAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerMediumAI))

    def test_choose_piece(self):
        """
        Tests choose_piece() and select() methods in the PlayerMediumAI class
        """
        test = PlayerMediumAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        test.game.pieces = {'10': '1010', '12': '1100', '13': '1101'}
        self.assertTrue(test.choose_piece() in ['10', '12', '13'])
        self.assertEqual('10', test.get_best(dict({str(pce): test.easy(test.
                         game.pieces[pce]) for pce in test.game.pieces}.
                                                  items()), True))
        self.assertEqual('12', test.get_best(dict({str(pce): test.easy(test.
                         game.pieces[pce]) for pce in test.game.pieces}.
                                                  items()), False))

    def test_place_piece(self):
        """
        Tests choose_piece() and select() methods in the PlayerMediumAI class
        """
        test = PlayerMediumAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        test.place_piece('1010')
        self.assertTrue(((test.game.board == [[None, '1000', '0001', '0101'],
                           ['1010', '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] or test.game.board
                          == [['1010', '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]) and not
                          test.game.has_won_game('1010')) or (test.game.board
                          == [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', '1010', '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] and
                            test.game.has_won_game('1010')))

    def test_player_ai_medium_play(self):
        """
        Tests average PlayerMediumAI player wins 50% +/- 10% in non-drawn games
        """
        p_one, p_two, count, wins = "Player One", "Player Two", 0, 0
        samples = 100  # the number of samples of won games in each test

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

    def test_player_ai_medium_vs_ai_easy_play(self):
        """
        Tests average MediumAI player wins >= 85% +/- 10% in non-drawn games
        """
        p_one, p_two, count, wins = "Player One", "Player Two", 0, 0
        samples = 100  # the number of samples of won games in each test

        while count < samples:
            test = Play()
            test.players = [PlayerMediumAI(test.game, p_one),
                            PlayerEasyAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto():
                count += 1

                if test.current_player.name == p_one:
                    wins += 1
        self.assertTrue(wins >= 75)

    def test_player_ai_medium_vs_ai_hard_play(self):
        """
        Tests average MediumAI player wins <= 15% +/- 10% in non-drawn games
        """
        p_one, p_two, count, wins = "Player One", "Player Two", 0, 0
        samples = 100  # the number of samples of won games in each test

        while count < samples:
            test = Play()
            test.players = [PlayerMediumAI(test.game, p_one),
                            PlayerHardAI(test.game, p_two)]
            test.current_player = choice(test.players)

            if test.play_auto():
                count += 1

                if test.current_player.name == p_one:
                    wins += 1
        self.assertTrue(wins <= 25)
