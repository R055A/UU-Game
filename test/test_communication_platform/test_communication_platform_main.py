#!/usr/bin/env python3

from unittest import TestCase, mock
from communication_platform.communication_platform import CommunicationPlatform


class TestCommunicationPlatform(TestCase):
    """
    Tests the CommunicationPlatform class
    Author(s): Adam Ross
    Date: 22/03/19
    """

    def test_communication_platform_main(self):
        """
        Tests CommunicationPlatform class instance
        """
        test = CommunicationPlatform()
        self.assertTrue(isinstance(test, CommunicationPlatform))

    def test_game_mode_options(self):
        """
        Tests the game_mode_options method when both local and online
        """
        test = CommunicationPlatform()
        with mock.patch('builtins.input', return_value="s"):
            self.assertEqual(test.game_mode_options("local"), "S")
        with mock.patch('builtins.input', return_value="t"):
            self.assertEqual(test.game_mode_options("local"), "T")
        with mock.patch('builtins.input', return_value="r"):
            self.assertEqual(test.game_mode_options("local"), "R")
        with mock.patch('builtins.input', return_value="q"):
            self.assertEqual(test.game_mode_options("local"), "Q")
        with mock.patch('builtins.input', return_value="s"):
            self.assertEqual(test.game_mode_options("online"), "S")
        with mock.patch('builtins.input', return_value="t"):
            self.assertEqual(test.game_mode_options("online"), "T")
        with mock.patch('builtins.input', return_value="r"):
            self.assertEqual(test.game_mode_options("online"), "R")
        with mock.patch('builtins.input', return_value="q"):
            self.assertEqual(test.game_mode_options("online"), "Q")

    def test_get_online_game_options(self):
        """
        Tests the get_online_game_options method
        """
        test = CommunicationPlatform()
        with mock.patch('builtins.input', return_value="s"):
            self.assertEqual(test.get_online_game_options(), "S")
        with mock.patch('builtins.input', return_value="j"):
            self.assertEqual(test.get_online_game_options(), "J")
        with mock.patch('builtins.input', return_value="r"):
            self.assertEqual(test.get_online_game_options(), "R")
        with mock.patch('builtins.input', return_value="q"):
            self.assertEqual(test.get_online_game_options(), "Q")

    def test_add_local_player(self):
        """
        Tests the add_local_player method
        """
        test = CommunicationPlatform()
        test.players = {"user": [True, 0]}
        with mock.patch('builtins.input', return_value="player_two"):
            test.add_local_player(2, 0)
        test.players.pop("user")
        self.assertEqual(list(test.players)[0], "Player_two")

    def test_choose_ai_difficulty(self):
        """
        Tests the choose_ai_difficulty method
        """
        test = CommunicationPlatform()
        with mock.patch('builtins.input', return_value="1"):
            self.assertEqual(test.choose_ai_difficulty(), "1")
        with mock.patch('builtins.input', return_value="2"):
            self.assertEqual(test.choose_ai_difficulty(), "2")
        with mock.patch('builtins.input', return_value="3"):
            self.assertEqual(test.choose_ai_difficulty(), "3")

    def test_decide_ai_players(self):
        """
        Tests the decide_ai_players method
        """
        test = CommunicationPlatform()
        test.user = "Nobody"
        with mock.patch('builtins.input', return_value="2"):
            test.decide_ai_players(2)
            self.assertEqual(len(test.players), 2)
        with mock.patch('builtins.input', return_value="1"):
            test.decide_ai_players(2)
            self.assertEqual(len(test.players), 2)
        with mock.patch('builtins.input', return_value="0"):
            test.decide_ai_players(2)
            self.assertEqual(len(test.players), 2)  # adds user "0"

    def test_decide_tour_players(self):
        """
        Tests the decide_tour_players method
        """
        test = CommunicationPlatform()
        with mock.patch('builtins.input', return_value="3"):
            self.assertEqual(test.decide_tour_players(), 3)
        with mock.patch('builtins.input', return_value="4"):
            self.assertEqual(test.decide_tour_players(), 4)
        with mock.patch('builtins.input', return_value="5"):
            self.assertEqual(test.decide_tour_players(), 5)
        with mock.patch('builtins.input', return_value="6"):
            self.assertEqual(test.decide_tour_players(), 6)
        with mock.patch('builtins.input', return_value="7"):
            self.assertEqual(test.decide_tour_players(), 7)
        with mock.patch('builtins.input', return_value="8"):
            self.assertEqual(test.decide_tour_players(), 8)

    def test_update_opp_players(self):
        """
        Tests the update_opp_players method
        """
        test = CommunicationPlatform()
        test.players = {"user": [True, 0]}
        test.update_opp_players({"user": [True, 0]})
        self.assertEqual(test.players, {"user": [True, 0], "user (guest)": [True, 0]})
