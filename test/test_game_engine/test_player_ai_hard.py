#!/usr/bin/env python3

from unittest import TestCase
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_hard import PlayerHardAI
from game_engine.game import Game
from random import choice
from game_platform.game_platform import GamePlatform


class TestPlayerAIHardClass(TestCase):
    """
    Tests the PlayerHardAI class
    Author(s): Adam Ross; Laurin Kerle
    Date: 22/03/19
    """

    def test_player_ai_hard(self):
        """
        Tests PlayerHardAI class instance
        """
        test = PlayerHardAI(Game(), "Test")
        self.assertTrue(isinstance(test, PlayerHardAI))

    # def test_choose_piece(self):
    #     """
    #     Tests choose_piece() method in the PlayerHardAI class
    #     """
    #     test = PlayerHardAI(Game(), "Test")
    #     test.game.board = [['0000', '1000', '0001', '0101'],
    #                         [None, '0010', '0111', None],
    #                         ['1001', None, '0100', '1111'],
    #                         ['1011', '0110', None, '1110']]
    #     test.game.pieces = {'3': '0011', '10': '1010',
    #                         '12': '1100', '13': '1101'}
    #     self.assertEqual('12', test.choose_piece())

    def test_place_piece(self):
        """
        Tests choose_piece() method in the PlayerHardAI class
        """
        test = PlayerHardAI(Game(), "Test")
        test.game.board = [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', None, '1111', '1011'],
                           ['0100', '0110', '0011', '1110']]
        test.game.pieces = {'10': '1010', '12': '1100', '13': '1101'}
        test.place_piece('1010')
        self.assertTrue(test.game.board
                          == [[None, '1000', '0001', '0101'],
                           [None, '0000', '0010', '0111'],
                           ['1001', '1010', '1111', '1011'],
                           ['0100', '0110', '0011', '1110']] and
                            test.game.has_won_game('1010'))

    def test_player_ai_hard_play(self):
        """
        Test HardAI for average wins against itself being <= 50%
        """
        average, samples = 0, 100  # samples of won games in each test

        for i in range(samples):
            test = GamePlatform("")
            test.play.players = [PlayerHardAI(test.play.game, "Player One"),
                                 PlayerHardAI(test.play.game, "Player Two")]
            test.play.current_player = choice(test.play.players)

            if test.play_local(True) and test.play.current_player.name == "Player One":
                average += 1
        self.assertTrue((average / samples * 100) <= 50)

    def test_player_ai_hard_vs_ai_easy_play(self):
        """
        Test HardAI for average wins against EasyAI being >= 90%
        """
        average, p_one, p_two = 0, "Player One", "Player Two"
        samples = 100  # the number of samples of won games in each test

        for i in range(samples):
            test = GamePlatform("")
            test.play.players = [PlayerHardAI(test.play.game, p_one),
                                 PlayerEasyAI(test.play.game, p_two)]
            test.play.current_player = choice(test.play.players)

            if test.play_local(True) and test.play.current_player.name == p_one:
                average += 1
        self.assertTrue((average / samples * 100) >= 95)
