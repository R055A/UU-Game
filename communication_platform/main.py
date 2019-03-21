#!/usr/bin/env python3

from os import system
from communication_platform.peer import Peer
from communication_platform.tournament import Tournament
from util.graphics import Graphics
from game_platform.game_platform import GamePlatform
from random import choice
from sys import exit


class CommunicationPlatform:
    """
    Communication platform main class
    Refactoring/integration editor(s): Adam Ross; Viktor Enzell;
                                       Gustav From; Pelle Ingvast
    Last-edit-date: 21/03/2019
    """

    NAME_LEN = 37  # the maximum length of a player's name
    ACK = "ACK"

    def __init__(self):
        """
        Class constructor
        """
        self.graphics = Graphics()  # Graphics class instance
        self.gp = None  # Play class instance - updated each game play
        self.ai_names = None  # the names of each available fictional AI player
        self.players = None  # dictionary for the player names and if users
        self.user = None  # the user name
        self.difficulty = 2  # the AI game play difficulty; 1 - 3; default 2
        self.automated = False  # Boolean for AI only games
        self.header = None  # a header for displaying above the game state

    def new_game(self, names):
        """
        Creates new Play and GamePlatform instances for each new game played
        """
        self.gp = GamePlatform(self.header)
        self.gp.play.init_players({names[0]: self.players[names[0]],
                                   names[1]: self.players[names[1]]})

    def start_comms(self):
        """
        A menu for selecting single or tournament game play or app termination
        """
        self.graphics.make_header("Welcome to UU-Game!")
        self.user = input("Enter player name: \n")[:self.NAME_LEN].capitalize()

        while True:
            play_choice = None

            while play_choice not in ["L", "O", "Q"]:
                print("Choose from the following " + self.graphics.
                      set_color("Y", "game play") + " options: ")
                print("    [" + self.graphics.set_color("G", "L") +
                      "] - Local\n    [" +
                      self.graphics.set_color("G", "O") +
                      "] - Online\n    [" +
                      self.graphics.set_color("R", "Q") + "] - Quit ")
                play_choice = input("Enter your " + self.graphics.
                                    set_color("G", "choice: \n")).upper()

            if play_choice == "L":  # user has selected a local game
                while True:
                    play_choice = self.game_mode_options("local")

                    if play_choice == "S":  # local singles game
                        play_choice = self.single_player_game()

                    elif play_choice == "T":  # local tournament game
                        play_choice = self.local_tournament()

                    if play_choice != "R" and play_choice != "Q":
                        continue
                    break

            elif play_choice == "O":  # user has selected online game
                while True:
                    play_choice = self.game_mode_options("online")

                    if play_choice == "S":  # Online singles game
                        play_choice = self.online_singles_options()

                    elif play_choice == "T":  # Online tournament game
                        play_choice = self.online_tournament_options()

                    if play_choice != "R" and play_choice != "Q":
                        continue
                    break

            if play_choice == "Q":  # user has selected to quit the game
                break

    def game_mode_options(self, game_mode):
        """
        Prints the options for choosing to play either singles or tournament
        :param game_mode: the selected local or online game play type
        :return: selected option of either singles, tournament, return or quit
        """
        print("Choose from the following " + self.graphics.
              set_color("Y", game_mode) + " options: ")
        print("    [" + self.graphics.set_color("G", "S") +
              "] - Singles (1 vs 1)\n    [" +
              self.graphics.set_color("G", "T") +
              "] - Tournament (3 - 8 players)\n    [" +
              self.graphics.set_color("G", "R") +
              "] - Return to previous options\n    [" +
              self.graphics.set_color("R", "Q") + "] - Quit")
        return input("Enter your " + self.graphics.
                     set_color("G", "choice: \n")).upper()

    def get_online_game_options(self):
        """
        Prompts user with online options for singles or tournament game
        :return: the chosen option by the user
        """
        print("Choose from one of the following " + self.graphics.
              set_color("Y", "online") + " options:\n    [" +
              self.graphics.set_color("G", "S") + "] - Start a new game\n"
              "    [" + self.graphics.set_color("G", "J") + "] - Join "
              "existing game\n    [" + self.graphics.set_color("G", "R") +
              "] - Return to previous menu\n    [" + self.graphics.
              set_color("R", "Q") + "] - Quit")
        return input("Enter your " + self.graphics.
                     set_color("G", "choice: \n")).upper()

    def online_singles_options(self):
        """
        A single player game played between against a remote player
        :return: the play_choice, which will be either "R" or "Q"
        """
        while True:
            play_choice = self.get_online_game_options()

            if play_choice == "S":
                play_choice = self.server_side_singles()

            elif play_choice == "J":
                play_choice = self.client_side_singles()

            if play_choice != "Q" and play_choice != "R":
                continue

            if play_choice == "R":
                play_choice = "0"
            return play_choice

    def online_tournament_options(self):
        """
        An online tournament played remotely between players
        :return: the resulting play choice for the main menu options
        """
        system('clear')
        self.graphics.make_header("Tournament play!")

        while True:
            play_choice = self.get_online_game_options()

            if play_choice == "S":
                play_choice = self.server_side_tournament()

            elif play_choice == "J":
                play_choice = self.client_side_tournament()

            if play_choice != "Q" and play_choice != "R":
                continue

            if play_choice == "R":
                play_choice = "0"
            return play_choice

    def single_player_game(self):
        """
        Local/Single player single (1 vs 1) game
        :return: '0' until the quit option during game play is implemented
        """
        system('clear')
        self.graphics.make_header("Local Match")
        self.decide_ai_players(2)

        if len(self.players) == 1:
            self.add_local_player(2, 1)
        self.header = list(self.players)[0] + " vs " + list(self.players)[1]

        while True:
            self.new_game([i for i in self.players.keys()])
            winner = self.gp.play_local(self.automated)

            if not winner:
                self.graphics.make_header("Draw!")
            else:
                self.graphics.make_header(winner + " won the game!")
                return "0"  # temporary until the quit option implemented

    def local_tournament(self):
        """
        A tournament locally between players
        :return: '0' until the quit option during game play is implemented
        """
        system('clear')
        self.graphics.make_header("Local Tournament!")

        while True:  # Decide number of players
            player_num = input("Choose the number of tournament players? [" +
                               self.graphics.set_color("G", "3 - 8") + "]\n")

            try:
                if 2 < int(player_num) < 9:
                    player_num = int(player_num)
                    break
            except:
                continue
        self.decide_ai_players(player_num)

        if len(self.players) != player_num:
            self.add_local_player(player_num, len(self.players))
        tour, winner = Tournament(list(self.players.keys())), None

        while True:
            self.graphics.make_header("Tournament Standings")
            print(tour.get_scoreboard())

            if tour.winner_state == 1:  # Last game already played
                break
            else:
                self.header = "Up next: " + tour.opponents[0] + " vs " +\
                              tour.opponents[1]

                while True:
                    self.new_game([tour.opponents[0], tour.opponents[1]])

                    if self.gp.play_local(self.automated) in \
                            [tour.opponents[0], tour.opponents[1]]:
                        break
                    else:
                        self.graphics.make_header("Draw game! Replaying game")
                tour.next_game(self.gp.play.current_player.name)  # Set winner
                self.graphics.make_header(self.gp.play.current_player.name +
                                          " has advanced to the next round!")
        self.graphics.make_header(self.gp.play.current_player.name +
                                  " has won the tournament!")
        return "0"  # temporary until the quit option implemented

    def server_side_singles(self):
        """
        The host side of an online singles game
        :return: '0' until the quit option during game play is implemented
        """
        peer = Peer(True)  # Peer conn as server

        if peer.start_server():
            peer.accept_client()
            peer.send(self.ACK)
            self.decide_ai_players(1, True)
            print("Waiting for opponent...")
            self.update_opp_players(peer.receive())  # Sync player lists
            peer.send(self.players)
            self.header = list(self.players)[0] + " vs " + list(self.players)[1]

            while True:
                self.new_game([i for i in self.players.keys()])
                peer.send({"play": self.gp, "auto": self.automated})
                game_result = self.gp.play_online(list(self.players)[0], peer,
                                                  self.automated)

                if game_result:
                    break
                else:
                    self.graphics.make_header("Game draw! Replay game")

            if game_result == list(self.players)[0]:
                self.graphics.make_header("You've won!")
            else:
                self.graphics.make_header("You've lost!")
            peer.teardown()
        return "0"  # temporary until the quit option implemented

    def client_side_singles(self):
        """
        The client side of an online singles game
        :return: '0' until the quit option during game play is implemented
        """
        peer = Peer(False)  # Create peer which will act as client

        if peer.connect_to_server():
            peer.receive()
            self.decide_ai_players(1)
            print("Waiting for opponent...")
            peer.send(self.players)
            self.players = peer.receive()

            while True:
                data = peer.receive()
                game_result = data["play"].play_online(list(self.players)[1],
                                                       peer, data["auto"])

                if game_result:
                    break
                else:
                    self.graphics.make_header("Game draw! Replay game")

            if game_result == list(self.players)[1]:
                self.graphics.make_header("You've won!")
            else:
                self.graphics.make_header("You've lost!")
            peer.teardown()
        return "0"  # temporary until the quit option implemented

    def server_side_tournament(self):
        """
        The host side of an online tournament game
        If multiple messages are sent in a row without being received,
        they will be concatenated in the pipeline and the receiving end
        will be unable to process the message. Therefor it is sometime
        needed to send junk messages to sync the clients.
        :return: '0' until the quit option during game play is implemented
        """
        peer = Peer(True, True)

        if peer.start_server():
            peer.accept_client()
            self.decide_ai_players(self.decide_tour_players() - 1, True)
            print("Waiting for opponent...")
            self.update_opp_players(peer.receive())  # Sync player lists
            peer.send(self.players)
            peer.receive()  # Block needed here to ensure clients are synced
            tour, data = Tournament(list(self.players.keys())), dict()
            data["instruction"] = data["players"] = None
            data["tour"], winner = tour.get_scoreboard(), ""

            while True:
                self.graphics.make_header("Tournament Standings")
                data["tour"] = tour.get_scoreboard()
                print(data["tour"])
                end, players, winners = tour.winner_state, tour.opponents, []

                if end == 1:  # Completed tournament
                    data["instruction"], data["player"] = "COMPLETE", winner
                    peer.send(data)
                    self.graphics.make_header(winner +
                                              " has won the tournament!")
                    peer.teardown()
                    break
                else:
                    data["players"], data["instruction"] = players, "PLAY"
                    peer.send(data)
                    self.header = "Up next: (local) " + players[0] + \
                                  " vs (remote) " + players[1]

                    while True:
                        self.new_game([tour.opponents[0], tour.opponents[1]])
                        peer.receive()
                        data["play"], data["auto"] = self.gp, self.automated
                        peer.send(data)
                        winner = self.gp.play_online(players[0], peer,
                                                     self.automated)

                        if winner:
                            break
                        else:
                            self.graphics.make_header("Game draw! Replay game")
                    winners.append(winner)
                    self.graphics.make_header(winner +
                                              " has advanced to next round!")
                tour.next_game(winner)
        return "0"  # temporary until the quit option implemented

    def client_side_tournament(self):
        """
        The client side of an online tournament game
        :return: '0' until the quit option during game play is implemented
        """
        peer = Peer(False, True)  # Setup

        if peer.connect_to_server():
            self.decide_ai_players(1)
            print("Waiting for opponent...")
            peer.send(self.players)  # Sync player lists
            self.players = peer.receive()
            peer.send(self.ACK)  # Sync with remote
            data = peer.receive()  # Get initial tournament bracket

            while True:
                self.graphics.make_header("Tournament Standings")
                print(data["tour"])

                if data["instruction"] == "COMPLETE":   # End tournament
                    self.graphics.make_header(data["player"] +
                                              " has won the tournament!")
                    peer.teardown()
                    break
                elif data["instruction"] == "PLAY":
                    players = data["players"]

                    while True:
                        peer.send(self.ACK)
                        data = peer.receive()
                        game_result = data["play"].play_online(players[1],
                                                               peer,
                                                               data["auto"])

                        if game_result:
                            break
                        else:
                            self.graphics.make_header("Game draw! Replay game")
                    self.graphics.make_header(game_result
                                              + " has advanced to next round!")
                data = peer.receive()
        return "0"  # temporary until the quit option implemented

    def add_local_player(self, nr_players, cur_num):
        """
        Prompts to enter user-controlled player names and adds to players dict
        :param nr_players: the total number of all players expected in the game
        :param cur_num: the total current players (AI or user) in the game
        """
        name = list(self.players.keys())[0]

        for i in range(2, nr_players - cur_num + 1):
            while name in self.players.keys():
                name = input("Enter user-controlled player #" + str(i) +
                             " name:\n")
            self.players[name[:self.NAME_LEN].capitalize()] = [True, 0]

    def choose_ai_difficulty(self):
        """
        Provides user with difficulty selection of easy, medium or hard
        :return: the difficulty selection of 1, 2, 3 for easy, medium or hard
        """
        print("Choose from one of the following " + self.graphics.
              set_color("Y", "AI difficulty") + " options:\n    [" + self.
              graphics.set_color("G", "1") + "] - Easy difficulty\n    [" +
              self.graphics.set_color("G", "2") +
              "] - Medium difficulty\n    [" + self.graphics.
              set_color("G", "3") + "] - Hard difficulty")
        return input("Enter your " + self.graphics.
                     set_color("G", "choice: \n")).upper()

    def decide_ai_players(self, nr_players, server=False):
        """
        Determines the number of AI players
        :param nr_players: the number of players in the game
        :param server: Boolean for if server player
        :return: the number of AI players in the game
        """
        while True:  # Decide number of AI players
            ai_num = input("Choose the number of AI players? [" + self.graphics
                           .set_color("G", "0 - " + str(nr_players)) + "]\n")

            try:
                if 0 <= int(ai_num) <= nr_players:
                    ai_num = int(ai_num)
                    break
            except:
                continue
        self.players = {self.user: [True, 0]}

        if server:
            self.ai_names = ["Ralph", "Randy", "Roger", "Rhys", "Rooster",
                             "Rob", "Ryan", "Richy", "Ross", "Ricky", "Rory"]
        else:
            self.ai_names = ["Viktor", "Peter", "Paul", "Chris", "Charles",
                             "Josh", "Steve", "Michael", "Larry", "Laurin"]
        self.players.update(dict({self.ai_names.pop(self.ai_names.index(choice(
            self.ai_names))): [False] for j in range(ai_num)}.items()))

        if nr_players == ai_num:
            self.players.pop(self.user)
            self.automated = True
        else:
            self.automated = False

        if ai_num > 0:
            while True:
                self.difficulty = self.choose_ai_difficulty()

                try:
                    if 1 <= int(self.difficulty) <= 3:
                        self.difficulty = int(self.difficulty)
                        break
                except:
                    continue
        else:
            self.difficulty = 0
        [self.players[i].append(self.difficulty)
         for i, j in self.players.items() if not j[0]]
        self.add_local_player(nr_players, ai_num)

    def decide_tour_players(self):
        """
        Determines the number of players for a tournament
        :return: the number of tournament players
        """
        while True:  # Decide number of players
            player_num = input("Choose the number of tournament players? [" +
                               self.graphics.set_color("G", "3 - 8") + "]\n")

            try:
                if 2 < int(player_num) < 9:
                    return int(player_num)
            except:
                continue

    def update_opp_players(self, opp_players):
        """
        Updates the player dictionary with the opponents (client) list
        :param opp_players: client player dictionary
        """
        for i in opp_players.keys():
            if i in self.players.keys():
                self.players[i + " (guest)"] = opp_players[i]
            else:
                self.players[i] = opp_players[i]

    def close_comms(self):
        """
        Prints a thank you message to the user and closes the program
        """
        self.graphics.make_header("Thanks for playing!")
        exit(1)
