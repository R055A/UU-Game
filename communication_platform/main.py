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
    Last-edit-date: 14/03/2019
    """

    NAME_LEN = 37  # the maximum length of a player's name

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
        self.server = False  # Boolean for playing online host
        self.automated = False  # Boolean for AI only games

    def new_game(self, names):
        """
        Creates new Play and GamePlatform instances for each new game played
        """
        self.automated = False
        self.gp = GamePlatform()
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
                        self.single_player_game()  # self.local_vs()

                    elif play_choice == "T":  # local tournament game
                        play_choice = self.local_tournament()

                    elif play_choice != "R" and play_choice != "Q":
                        continue
                    break

            elif play_choice == "O":  # user has selected online game
                while True:
                    self.server = False
                    play_choice = self.game_mode_options("online")

                    if play_choice == "S":  # Online singles game
                        play_choice = self.online_singles_options()

                    elif play_choice == "T":  # Online tournament game
                        play_choice = self.online_tournament_options()

                    elif play_choice != "R" and play_choice != "Q":
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
              "] - Return to main menu\n    [" + self.graphics.
              set_color("R", "Q") + "] - Quit")
        return input("Enter your " + self.graphics.
                     set_color("G", "choice: \n")).upper()

    def online_singles_options(self):
        """
        A single player game played between against a remote player
        """
        while True:
            play_choice = self.get_online_game_options()

            if play_choice == "S":
                self.server_side_singles()
                continue

            elif play_choice == "J":
                self.client_side_singles()
                continue

            elif play_choice == "Q":
                return "Q"

            if play_choice in ["S", "J", "R"]:
                return "R"

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
                self.server_side_tournament()
                continue

            elif play_choice == "J":
                self.client_side_tournament()
                continue

            elif play_choice == "Q":
                return "Q"

            if play_choice in ["S", "J", "R"]:
                return "R"

    def single_player_game(self):
        """
        Local/Single player single (1 vs 1) game
        :return: the "Return" play choice for returning to the main menu option
        """
        system('clear')
        self.graphics.make_header("Local Match")

        while True:
            self.decide_ai_players(2, False)

            if len(self.players) == 1:
                self.add_local_player()
            self.new_game([i for i in self.players.keys()])
            winner = self.gp.play_local(self.automated)

            if not winner:
                self.graphics.make_header("Draw!")
            else:
                self.graphics.make_header(winner + " won the game!")
                return "R"

    def local_tournament(self):
        """
        A tournament locally between players
        :return: the "Return" play choice for returning to the main menu option
        """
        system('clear')
        self.graphics.make_header("Local Tournament!")

        while True:  # Decide number of players
            player_num = input("Choose the number of tournament players? [" +
                               self.graphics.set_color("G", "3 - 8") + "]\n")

            try:
                if 2 < int(player_num) < 9:
                    break
            except:
                continue
        self.decide_ai_players(int(player_num), False)

        while int(player_num) > len(self.players):
            self.add_local_player()
        tour, winner = Tournament(list(self.players.keys())), None

        while True:
            self.graphics.make_header("Tournament Standings")
            print(tour.get_scoreboard())

            if tour.winner_state == 1:  # Last game already played
                break
            else:
                self.graphics.make_header("Up next: " + tour.opponents[0]
                                          + " vs " + tour.opponents[1])

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
        return "R"

    def server_side_singles(self):
        """
        The host side of an online singles game
        """
        self.server = True
        peer = Peer(self.server)  # Peer conn as server
        peer.accept_client()
        peer.send("ACK")
        self.decide_ai_players(1, True)
        self.players.update(peer.receive())

        while True:
            self.new_game([i for i in self.players.keys()])
            peer.send({"play": self.gp, "auto": self.automated})
            win = self.gp.online_vs(self.user, peer, self.server,
                                    self.automated)

            if win != "DRAW":
                break
            else:
                self.graphics.make_header("Game draw! Replay game")

        if win == self.user:
            self.graphics.make_header("You've won!")
        else:
            self.graphics.make_header("You've lost!")
        peer.teardown()

    def client_side_singles(self):
        """
        The client side of an online singles game
        """
        peer = Peer(self.server)  # Create peer which will act as client
        peer.connect_to_server()
        peer.receive()
        self.decide_ai_players(1, True)
        peer.send(self.players)

        while True:
            data = peer.receive()
            win = data["play"].online_vs(self.user, peer, self.server,
                                         data["auto"])

            if win != "DRAW":
                break
            else:
                self.graphics.make_header("Game draw! Replay game")

        if win == self.user:
            self.graphics.make_header("You've won!")
        else:
            self.graphics.make_header("You've lost!")
        peer.teardown()

    def server_side_tournament(self):
        """
        The host side of an online tournament game
        If multiple messages are sent in a row without being received,
        they will be concatenated in the pipeline and the receiving end
        will be unable to process the message. Therefor it is sometime
        needed to send junk messages to sync the clients.
        """
        self.server = True  # Setup
        peer = Peer(self.server)
        peer.accept_client()
        self.decide_online_tour_players(peer)
        print("Waiting for remote list of players...")
        opp_players = peer.receive()  # Sync player lists
        peer.send(self.players)

        for i in opp_players.keys():
            if i in self.players.keys():
                self.players[i + " (opponent)"] = opp_players[i]
            else:
                self.players[i] = opp_players[i]
        peer.receive()  # Block needed here to ensure clients are synced
        tour = Tournament(list(self.players.keys()))  # Create tournament
        data = dict()  # Dictionary containing various data needed by remote peer
        data["instruction"] = None  # Instructions in the form of strings
        data["players"] = None  # players to play next game
        data["tour"] = tour.get_scoreboard()  # String for tournament bracket
        # peer.send(data)  # Send initial tournament bracket
        winner = ""

        while True:
            self.graphics.make_header("Tournament Standings")
            data["tour"] = tour.get_scoreboard()
            print(data["tour"])
            end = tour.winner_state
            players = tour.opponents
            winners = []

            if end == 1:  # Completed tournament
                data["instruction"] = "COMPLETE"
                data["player"] = winner
                peer.send(data)
                self.graphics.make_header(winner + " has won the tournament!")
                peer.teardown()
                break
            else:
                data["players"] = players
                data["instruction"] = "PLAY"
                peer.send(data)
                self.graphics.make_header("Up next: (local) " + players[0] +
                                          " vs (remote) " + players[1])

                while True:
                    self.new_game([tour.opponents[0], tour.opponents[1]])
                    peer.receive()
                    data["play"] = self.gp
                    data["auto"] = self.automated
                    peer.send(data)
                    winner = self.gp.online_vs(players[0], peer, self.server,
                                               self.automated)

                    if winner != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")

                if winner == players[0]:  # If local player won
                    winners.append(winner)
                    self.graphics.make_header(winner +
                                              " has advanced to next round!")
                else:  # If remote player won
                    winner = players[1]
                    winners.append(winner)
                    self.graphics.make_header(winner
                                              + " has advanced to next round!")
            tour.next_game(winner)

    def client_side_tournament(self):
        """
        The client side of an online tournament game.
        """
        self.server = False
        peer = Peer(False)  # Setup
        peer.connect_to_server()
        self.decide_online_tour_players(peer)
        peer.send(self.players)  # Sync player lists
        opp_players = peer.receive()

        for i in opp_players.keys():
            if i in self.players.keys():
                self.players[i + " (opponent)"] = opp_players[i]
            else:
                self.players[i] = opp_players[i]
        peer.send("ACK")  # Sync with remote
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
                self.graphics.make_header("Up next: (local) " + players[1] +
                                          " vs (remote) " + players[0])

                while True:
                    peer.send("ACK")
                    data = peer.receive()
                    winner = data["play"].online_vs(players[1], peer,
                                                    self.server, data["auto"])

                    if winner != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")

                if winner == players[1]:  # If local player won
                    self.graphics.make_header(winner
                                              + " has advanced to next round!")
                else:  # If remote player won
                    self.graphics.make_header(players[0]
                                              + " has advanced to next round!")
            data = peer.receive()

    def add_local_player(self):
        """
        Prompts user to enter second user player name and adds to players dict
        """
        self.players[input("Enter 2nd user name")[:self.NAME_LEN]] = [True, 0]

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

    def decide_ai_players(self, nr_players, online):
        """
        Determines the number of AI players
        :param nr_players: the number of players in the game
        :param online: Boolean for if game is online or not
        :return: the number of AI players in the game
        """
        if online:
            start = str(nr_players - 1)
        else:
            start = "0"

        while True:  # Decide number of AI players
            ai_num = input("Choose the number of AI players? [" + self.
                           graphics.set_color("G", start + " - " +
                                              str(nr_players)) + "]\n")

            try:
                if 0 <= int(ai_num) <= nr_players:
                    ai_num = int(ai_num)
                    break
            except:
                continue
        self.players = {self.user: [True, 0]}

        if self.server:
            self.ai_names = ["Ralph", "Randy", "Roger", "Rhys", "Rooster",
                             "Rob", "Ryan", "Richy", "Ross", "Ricky", "Rory"]
        else:
            self.ai_names = ["Viktor", "Peter", "Paul", "Chris", "Charles",
                             "Josh", "Steve", "Michael", "Larry", "Laurin"]
        self.players.update(dict({self.ai_names.pop(self.ai_names.index(choice(
            self.ai_names))): [False] for j in range(ai_num)}.items()))

        if nr_players == ai_num:
            self.players.pop(self.user)

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

    def decide_online_tour_players(self, peer):
        """
        Determines the number of players between host and client users
        :param peer: peer is connection between host and client
        """
        if not self.server:
            print("Confirming number of host controlled tournament players...")
            nr_plyrs = str(8 - int(peer.receive()))
            print("Host player has chosen to control " + nr_plyrs +
                  " tournament players")
        else:
            nr_plyrs = "7"

        while True:
            if nr_plyrs == "7":
                start = "2"
            else:
                start = "1"

            try:
                nr = input("Choose a number of tournament players: [" + self.
                           graphics.set_color("G", start + " - " + nr_plyrs) +
                           "]\n")

                if 1 <= int(nr) <= int(nr_plyrs):
                    if self.server:
                        peer.send(nr)  # Send number of players to peer conn
                    break
            except:
                continue
        peer.send("ACK")
        peer.receive()
        self.decide_ai_players(int(nr), True)

    def close_comms(self):
        """
        Prints a thank you message to the user and closes the program
        """
        self.graphics.make_header("Thanks for playing!")
        exit(1)
