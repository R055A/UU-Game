#!/usr/bin/env python3

from unittest import TestCase
from communication_platform.tournament import Tournament
import random

NUM_PLAYERS = 8  # the number of players in a tournament


class TestTournament(TestCase):
    """
    Tests the Tournament class
    Author(s): Adam Ross
    Date: 22/03/19
    """

    def test_tournament(self):
        """
        Tests Tournament class instance
        """
        test = Tournament(['random_name_one', 'random_name_two', 'random_name_three'])
        self.assertTrue(isinstance(test, Tournament))


def main():
    """
    Tests tournament class and bracket displaying
    """
    players, player_list = NUM_PLAYERS, []
    player_name = ["Pettersson", "Undran", "Ola", "Mr.X", "Bumbi-Bu",
                   "Pelle", "Gerald", "Ronald", "Nisse", "Megamen",
                   "Baby-Jesus", "Tyke", "Kim", "Q"]

    for i in range(players):
        temp = random.choice(player_name)
        player_name.remove(temp)
        player_list.append(temp)
    test = Tournament(player_list)
    print(test.get_scoreboard())

    while test.winner_state == 0:
        print("Players waiting: ", test.waiting_players)
        random_number = random.randint(0, 1)
        print("All Opponents: ", test.all_opponents)
        print("Opponents queue: ", test.opponents_queue)
        print("Opponents: ", test.opponents)
        winner = test.opponents[random_number]
        print("Winner_list_temp: ", test.winner_list_temp)
        print("Winner_list: ", test.winner_list)
        print("Winners this game: ", winner)
        print()
        print("-------------------------------------------------------------")
        test.next_game(winner)
        print(test.get_scoreboard())
    print("Winner_list: ", test.winner_list)
    print("OPPONENTS: ", test.all_opponents)
    print("WINNER: ", test.winner_list[test.tournament_depth - 1][0])


if __name__ == "__main__":
    main()
