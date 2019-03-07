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
    Last-edit-date: 06/03/2019
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
        self.server = False  # Boolean for playing multi-player online host
        self.automated = False  # Boolean for AI only games

    def new_game(self, names):
        """
        Creates new Play and GamePlatform instances for each new game played
        """
        self.automated = False
        self.gp = GamePlatform()

        if self.players[names[0]] and self.players[names[1]]:
            self.gp.play.init_players(1, self.difficulty, names[0], names[1])
        elif self.players[names[1]]:
            self.gp.play.init_players(2, self.difficulty, names[1], names[0])
        elif self.players[names[0]]:
            self.gp.play.init_players(2, self.difficulty, names[0], names[1])
        else:
            self.automated = True
            self.gp.play.init_players(3, self.difficulty, names[0], names[1])

    def start_comms(self):
        """
        A menu for selecting single or tournament game play or app termination
        """
        self.graphics.make_header("Welcome to UU-Game!")
        self.user = input("Enter player name: \n")[:self.NAME_LEN].capitalize()

        while True:
            play_choice = None

            while play_choice not in ["S", "M", "Q"]:
                print("Choose from the following " + self.graphics.
                      set_color("Y", "game play") + " options: ")
                print("    [" + self.graphics.set_color("G", "S") +
                      "] - Single player\n    [" +
                      self.graphics.set_color("G", "M") +
                      "] - Multi-player\n    [" +
                      self.graphics.set_color("R", "Q") + "] - Quit ")
                play_choice = input("Enter your " + self.graphics.
                                    set_color("G", "choice: \n")).upper()

            if play_choice == "S":  # user has selected a single player game
                while True:
                    play_choice = self.game_mode_options("single player")

                    if play_choice == "S":  # Single player singles game
                        self.single_player_game()  # self.local_vs()

                    elif play_choice == "T":  # Single player tournament game
                        play_choice = self.single_player_tournament()

                    elif play_choice != "R" and play_choice != "Q":
                        continue
                    break

            elif play_choice == "M":  # user has selected multi-player game
                while True:
                    self.server = False
                    play_choice = self.game_mode_options("multi-player")

                    if play_choice == "S":  # Multi-player singles game
                        play_choice = self.multiplayer_singles_options()

                    elif play_choice == "T":  # Multi-player tournament game
                        play_choice = self.multiplayer_tournament_options()

                    elif play_choice != "R" and play_choice != "Q":
                        continue
                    break

            if play_choice == "Q":  # user has selected to quit the game
                break

    def game_mode_options(self, game_mode):
        """
        Prints the options for choosing to play either singles or tournament
        :param game_mode: the selected single or multi-player game play type
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

    def get_multiplayer_game_options(self):
        """
        Prompts user with multiplayer options for singles or tournament game
        :return: the chosen option by the user
        """
        print("Choose from one of the following " + self.graphics.
              set_color("Y", "multi-player") + " options:\n    [" +
              self.graphics.set_color("G", "S") + "] - Start a new game\n"
              "    [" + self.graphics.set_color("G", "J") + "] - Join "
              "existing game\n    [" + self.graphics.set_color("G", "R") +
              "] - Return to main menu\n    [" + self.graphics.
              set_color("R", "Q") + "] - Quit")
        return input("Enter your " + self.graphics.
                     set_color("G", "choice: \n")).upper()

    def multiplayer_singles_options(self):
        """
        A single player game played between against a remote player
        """
        while True:
            play_choice = self.get_multiplayer_game_options()

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

    def multiplayer_tournament_options(self):
        """
        A multi-player tournament played remotely between players
        :return: the resulting play choice for the main menu options
        """
        system('clear')
        self.graphics.make_header("Tournament play!")

        while True:
            play_choice = self.get_multiplayer_game_options()

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

        :return:
        """
        system('clear')
        self.graphics.make_header("Single Player Match")

        while True:
            choice = self.setup_single_choice()

            if choice == "1":
                play2_name = input("Enter opponent's name: ")[:self.NAME_LEN]
                self.players = {self.user: True, play2_name: True}
                self.new_game([self.user, play2_name])
                winner = self.gp.play_local()

                if not winner:
                    self.graphics.make_header("Draw!")
                else:
                    self.graphics.make_header(winner + " won the game!")
                return "R"
            
            elif choice == "2":
                print("User vs AI")
                self.setup_ai_difficulty(1)
                ai_name = input("Enter opponent AI name: ")[:self.NAME_LEN]
                self.players = {self.user: True, ai_name: False}
                self.new_game([self.user, ai_name])
                winner = self.gp.play_local()

                if not winner:
                    self.graphics.make_header("Draw!\n")
                else:
                    self.graphics.make_header(winner + " won the game!")
                return "R"
                
            elif choice == "3":
                print("AI vs AI")
                self.setup_ai_difficulty(2)
                self.players = {"Player One": False, "Player Two": False}
                self.new_game(["Player One", "Player Two"])
                winner = self.gp.play_local()

                if not winner:
                    self.graphics.make_header("Draw!")
                else:
                    self.graphics.make_header(winner + " won the game!")
                return "R"

    def single_player_tournament(self):
        """
        A single-player tournament locally between players
        :return: the "Return" play choice for returning to the main menu option
        """
        system('clear')
        self.graphics.make_header("Single Player Tournament!")

        while True:  # Decide number of players
            player_num = input("Choose the number of tournament players? [" +
                               self.graphics.set_color("G", "3 - 8") + "]\n")

            try:
                if 2 < int(player_num) < 9:
                    break
            except:
                continue
        ai_num = self.setup_ai_players(int(player_num))
        self.setup_ai_difficulty(ai_num)
        self.setup_player_names(player_num, ai_num)
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

                    if self.gp.play_local() in [tour.opponents[0],
                                                tour.opponents[1]]:
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

        if self.decide_online_ai_players(peer, 1) > 0:
            self.players = {self.user: False}
        else:
            self.players = {self.user: True}
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

        if self.decide_online_ai_players(peer, 1) > 0:
            self.players = {self.user: False}
        else:
            self.players = {self.user: True}
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

    def setup_ai_difficulty(self, ai_num):
        """
        User chooses an AI difficulty between 1 and 3, or 0 default
        :param ai_num: the chosen number of AI players
        """
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
            
    def setup_single_choice(self):
        """
        User chooses an option of gamemode between 1 and 3,
         huvshu, huvsai or aivsai ????
        :return: The chooses of game mode
        """
        while True:
            print("Choose from one of the following options:\n    [" + self.
                  graphics.set_color("G", "1") + "] - User vs User\n    [" +
                  self.graphics.set_color("G", "2") + "] - User vs AI\n    [" +
                  self.graphics.set_color("G", "3") + "] - AI vs AI")
            choice = input("Enter your " + self.graphics.
                           set_color("G", "choice: \n")).upper()

            try:
                if 1 <= int(choice) <= 3:
                    return choice
            except:
                continue

    def setup_ai_players(self, player_num):
        """
        Determine names and human/computer controlled
        :param player_num: the number of players in the game
        :return: the number of ai players
        """
        while True:  # Decide number of AI players
            ai_num = input("Choose the number of AI players? [" + self.
                           graphics.set_color("G", "0 - " + str(player_num)) +
                           "]\n")

            try:
                if 0 <= int(ai_num) <= player_num:
                    print("Confirming opponents choice of AI players...")
                    return int(ai_num)
            except:
                continue

    def setup_player_names(self, user_num, ai_num=0):
        """
        Where user player names are entered and AI names randomly generated
        ALso creates a new Play instance and resets the player and AI names
        :param user_num: the number of user players
        :param ai_num: the number of AI players
        """
        self.players = {self.user: True}

        if self.server:
            self.ai_names = ["Ralph", "Randy", "Roger", "Rhys", "Rooster",
                            "Rob", "Ryan", "Richy", "Ross", "Ricky", "Rory"]
        else:
            self.ai_names = ["Viktor", "Peter", "Paul", "Chris", "Charles",
                            "Josh", "Steve", "Michael", "Larry", "Laurin"]

        for i in range(len(self.players), int(user_num) - int(ai_num)):
            name = input("Enter a unique player " + str(i) +
                         " name:\n")[:self.NAME_LEN].capitalize()

            while name in self.players.keys():
                name = input("Enter a unique player " + str(i) +
                             " name:\n")[:self.NAME_LEN].capitalize()
            self.players[name] = True
        self.players.update(dict({self.ai_names.pop(self.ai_names.index(choice(
            self.ai_names))): False for j in range(int(ai_num))}.items()))

        if int(user_num) == int(ai_num):
            self.players.pop(self.user)

    def decide_online_ai_players(self, peer, nr_players):
        """
        Determines the number of AI players between host and client users
        :param peer: connection between host and client
        :param nr_players: the number of players in game
        :return: the number of AI players in the game
        """
        ai_num = self.setup_ai_players(nr_players)
        peer.send("ACK")
        peer.receive()
        receive_diff = False

        if ai_num > 0 and self.server:
            self.setup_ai_difficulty(ai_num)
            peer.send(self.difficulty)
            peer.receive()
        elif ai_num == 0 and self.server:
            peer.send(0)
            print("Confirming the client AI selection...")
            self.difficulty = int(peer.receive())

            if self.difficulty != 0:
                print("Confirming the client AI difficulty selection...")
                receive_diff = True
        else:
            print("Confirming the host AI selection...")
            self.difficulty = int(peer.receive())

            if self.difficulty == 0:
                if ai_num > 0:
                    self.setup_ai_difficulty(ai_num)
                    peer.send(self.difficulty)
                else:
                    peer.send(0)
            else:
                print("Confirming the host AI difficulty selection...")
                receive_diff = True
                peer.send(0)

        if receive_diff:
            if self.difficulty == 1:
                diff = "easy"
            elif self.difficulty == 2:
                diff = "medium"
            else:
                diff = "hard"
            print("AI difficulty is " + diff)
        return ai_num

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
            try:
                nr = input("Choose a number of players to control: [" + self.
                           graphics.set_color("G", "1 - " + nr_plyrs) + "]\n")

                if 1 <= int(nr) <= int(nr_plyrs):
                    if self.server:
                        peer.send(nr)  # Send number of players to peer conn
                    break
            except:
                continue
        ai_num = self.decide_online_ai_players(peer, int(nr))
        self.setup_player_names(int(nr), ai_num)

    def close_comms(self):
        """
        Prints a thank you message to the user and closes the program
        """
        self.graphics.make_header("Thanks for playing!")
        exit(1)
