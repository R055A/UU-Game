#!/usr/bin/env python3

from unittest import TestCase
from game_engine.game import Game
from game_engine.game_engine import GameEngine
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_ai_hard import PlayerHardAI
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_human import PlayerHuman


class TestGameEngineClass(TestCase):
    """
    Tests the GameEngine class, its init variables, and its methods
    Author: Adam Ross
    Date: 22/03/19
    """

    def test_game_engine(self):
        """
        Tests GameEngine class instance
        """
        test = GameEngine()
        self.assertTrue(isinstance(test, GameEngine))

    def test_game_instance(self):
        """
        Tests Game instance in GameEngine class instance
        """
        test = GameEngine()
        self.assertTrue(isinstance(test.game, Game))

    def test_players_init_human(self):
        """
        Tests initiated players for two user players
        """
        test = GameEngine()
        self.assertEqual(test.players, [])
        test.init_players({"Caesar": [True, 0], "Augustus": [True, 0]})
        self.assertEqual(len(test.players), 2)

        for i in range(2):
            self.assertTrue(isinstance(test.players[i], PlayerHuman))

    def test_players_init_ai_medium_easy(self):
        """
        Tests initiated players for AI medium and easy players
        """
        test = GameEngine()
        self.assertEqual(test.players, [])
        test.init_players({"R2-D2": [False, 2], "C-3PO": [False, 1]})
        self.assertEqual(len(test.players), 2)
        self.assertTrue(isinstance(test.players[0], PlayerMediumAI))
        self.assertTrue(isinstance(test.players[1], PlayerEasyAI))

    def test_players_init_ai_medium_hard(self):
        """
        Tests initiated players for AI medium and hard players
        """
        test = GameEngine()
        self.assertEqual(test.players, [])
        test.init_players({"T-800": [False, 2], "T-1000": [False, 3]})
        self.assertEqual(len(test.players), 2)
        self.assertTrue(isinstance(test.players[0], PlayerMediumAI))
        self.assertTrue(isinstance(test.players[1], PlayerHardAI))

    def test_players_init_ai_easy_hard(self):
        """
        Tests initiated players for AI easy and hard players
        """
        test = GameEngine()
        self.assertEqual(test.players, [])
        test.init_players({"Hermie": [False, 1], "David": [False, 3]})
        self.assertEqual(len(test.players), 2)
        self.assertTrue(isinstance(test.players[0], PlayerEasyAI))
        self.assertTrue(isinstance(test.players[1], PlayerHardAI))

    def test_players_init_user_ai(self):
        """
        Tests initiated players for user and AI players
        """
        test = GameEngine()
        self.assertEqual(test.players, [])
        test.init_players({"Fry": [True, 0], "Bender": [False, 2]})
        self.assertEqual(len(test.players), 2)
        self.assertTrue(isinstance(test.players[0], PlayerHuman))
        self.assertTrue(isinstance(test.players[1], PlayerMediumAI))

    def test_current_and_change_player(self):
        """
        Tests current_player variable and change_player() method
        in Play class instance
        """
        test = GameEngine()
        self.assertEqual(test.current_player, None)
        test.init_players({"KITT": [False, 3], "Michael Knight": [True, 0]})
        player_one = test.current_player
        self.assertTrue(isinstance(player_one, PlayerHardAI))
        player_two = test.change_player()
        self.assertTrue(isinstance(player_two, PlayerHuman))
        self.assertNotEqual(player_one, player_two)

    def test_selected_piece(self):
        """
        Tests selected_piece variable in Play class instance
        """
        test = GameEngine()
        self.assertEqual(test.selected_piece, None)
        test.selected_piece = test.game.pieces['0']
        self.assertEqual(test.selected_piece, '0000')
        self.assertEqual(test.selected_piece, test.game.pieces['0'])
