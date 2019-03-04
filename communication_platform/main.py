#!/usr/bin/env python3

import communication_platform.game as game
from communication_platform.peer import Peer
from communication_platform.tournament import Tournament
from communication_platform.graphics import Graphics
from game_platform.game_platform import GamePlatform
from game_engine.play import Play
from game_engine.player_human import PlayerHuman
from random import choice
from sys import exit


class CommunicationPlatform:
    """
    Communication platform main class
    Refactoring/integration editor(s): Adam Ross; Viktor Enzell; Gustav From;
                                       Pelle Ingvast
    Last-edit-date: 27/02/2019
    """

    NAME_LEN = 20  # the maximum length of a player's name

    def __init__(self):
        """
        Class constructor
        """
        self.graphics = Graphics()  # Graphics class instance
        self.play = None  # Play class instance - updated each game play
        self.game_platform = None  # GamePlatform class instance
        self.ai_names = None  # the names of each available fictional AI player
        self.players = None  # dictionary for the player names and if users
        self.user = None  # the user name
        self.difficulty = 2  # the AI game play difficulty; 1 - 3; default 2
        self.server = False  # Boolean for playing multi-player online host

    def new_game(self):
        """
        Creates new Play and GamePlatform instances for each new game played
        """
        self.play = Play()
        self.game_platform = GamePlatform(self.play)

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
                        pass  # self.local_vs()

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
                        play_choice = self.online_vs()

                    elif play_choice == "T":  # Multi-player tournament game
                        play_choice = self.multiplayer_tournament()

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

    # def local_vs(self):
    #     """
    #     Sig:    None
    #     Pre:    None
    #     Post:   A game played between between two players
    #     """
    #     #players, humans = self.get_local_names()
    #     while True:
    #         result = game.local_vs(players, humans)
    #         if result != "DRAW":
    #             break
    #         else:
    #             g.make_header("Game draw! Replay game")
    #     self.graphics.make_header(result + " has won!")

    def online_vs(self):
        """
        A single player game played between against a remote player
        """
        while True:
            play_choice = self.get_multiplayer_game_options()

            if play_choice == "S":
                self.server_side_singles()

            elif play_choice == "J":
                self.client_side_singles()

            elif play_choice == "Q":
                return "Q"

            if play_choice in ["S", "J", "R"]:
                return "R"

    def server_side_singles(self):
        """
        The host side of an online singles game
        """
        self.server = True
        self.new_game()
        peer = Peer(self.server)  # Create peer which will act as server
        peer.accept_client()
        peer.send(self.play)

        while True:
            win = game.online_vs(self.user, peer, True, self.server, self.play)

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

        while True:
            win = game.online_vs(self.user, peer, True, self.server,
                                 peer.receive())

            if win != "DRAW":
                break
            else:
                self.graphics.make_header("Game draw! Replay game")
        if win == self.user:
            self.graphics.make_header("You've won!")
        else:
            self.graphics.make_header("You've lost!")
        peer.teardown()

    def setup_tournament_game(self, tournament):
        """
        Initializes a tournament game in preparation for playing
        :param tournament: the tournament players playing a game
        :return: the game mode; whether player vs player, AI vs AI...
        """
        if self.players[tournament.opponents[0]] and \
                self.players[tournament.opponents[1]]:
            mode = 1
        elif self.players[tournament.opponents[0]] or \
                self.players[tournament.opponents[1]]:
            if self.players[tournament.opponents[1]]:
                tournament.opponents[0], tournament.opponents[1] = \
                    tournament.opponents[1], tournament.opponents[0]
            mode = 2
        else:
            mode = 3
        return mode

    def declare_available_pieces(self):  # TEMPORARY UNTIL WE HAVE A GAME PLATFORM ---------------------------------
        """
        Declares to the players the pieces available for selection
        Temporary for the CLI testing
        """
        print("\nGame pieces status:")
        print(list(self.play.game.pieces.items())[:int((len(self.play.game.
                                                            pieces) + 1) / 2)])

        if len(self.play.game.pieces) > 1:
            print(list(self.play.game.pieces.
                       items())[int((len(self.play.game.pieces) + 1) / 2):])

    def declare_board_status(self):  # TEMPORARY UNTIL WE HAVE A GAME PLATFORM ---------------------------------
        """
        Declares to the players the current status of the game board
        Temporary for the CLI testing
        """
        print("\nGame board status:")
        print(*(row for row in self.play.game.board), sep="\n")

    def declare_current_player(self):  # TEMPORARY UNTIL WE HAVE A GAME PLATFORM ---------------------------------
        """
        Temporary printing of current player for CLI testing and presenting
        """
        print("\nCurrent player: '" + self.play.current_player.name + "'")

    def declare_selected_piece(self):  # TEMPORARY UNTIL WE HAVE A GAME PLATFORM ---------------------------------
        """
        Temporary printing of selected piece for CLI testing and presenting
        """
        print("\nCurrent piece: " + str(self.play.selected_piece))

    def play_manual(self):
        """
        Plays manual game between either player vs player or player vs AI game
        :return: the winner's name or None for a draw
        """
        while True:
            self.declare_available_pieces()  # prints game board status
            self.declare_board_status()  # prints available pieces status

            if isinstance(self.play.current_player, PlayerHuman):
                while True:
                    pce = input("\nEnter number 0-15 of piece selection: ")

                    if self.play.play_selection(pce):
                        break
            else:
                self.play.play_selection()
            self.declare_selected_piece()  # prints the selected piece
            self.declare_current_player()  # prints the current player turn

            if isinstance(self.play.current_player, PlayerHuman):
                while True:
                    try:
                        y, x = input("\nEnter 2 ints 0-3 separated by a space: ").\
                            split()

                        if self.play.play_placement(y, x):
                            break
                    except:
                        continue
            else:
                self.play.play_placement()

            if self.play.game.has_won_game(self.play.selected_piece):
                self.declare_board_status()  # prints final status of board
                return self.play.current_player.name
            elif not self.play.game.has_next_play():  # checks if turns remaining
                self.declare_board_status()  # prints final status of board
                return None

    def single_player_tournament(self):
        """
        A single-player tournament locally between players
        :return: the "Return" play choice for returning to the main menu option
        """
        self.graphics.make_header("Single Player Tournament!")
        self.setup_tournament_players()
        tournament, winner = Tournament(list(self.players.keys())), None

        while True:
            self.graphics.make_header("Tournament Standings")
            tournament.get_scoreboard()

            if tournament.winner_state == 1:  # Last game already played
                break
            else:
                self.graphics.make_header("Up next: " + tournament.opponents[0]
                                          + " vs " + tournament.opponents[1])
                mode = self.setup_tournament_game(tournament)

                while True:
                    self.new_game()
                    self.play.init_players(mode, self.difficulty,
                                           tournament.opponents[0],
                                           tournament.opponents[1])
                    self.declare_current_player()  # TEMPORARY UNTIL WE HAVE A GAME PLATFORM -------------------------

                    if mode == 3:
                        if self.play.play_auto():
                            break
                    elif self.play_manual() in [tournament.opponents[0],
                                                tournament.opponents[1]]:
                        break
                    else:
                        self.graphics.make_header("Draw game! Replaying game")
                tournament.next_game(self.play.current_player.name)  # Set winner
                self.graphics.make_header(self.play.current_player.name +
                                          " has advanced to the next round!")
        self.graphics.make_header(self.play.current_player.name +
                                  " has won the tournament!")
        return "R"

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

    def multiplayer_tournament(self):
        """
        A multi-player tournament played remotely between players
        :return: the resulting play choice for the main menu options
        """
        self.graphics.make_header("Tournament play!")

        while True:
            play_choice = self.get_multiplayer_game_options()

            if play_choice == "S":
                self.server_side_tournament()

            elif play_choice == "J":
                self.client_side_tournament()

            elif play_choice == "Q":
                return "Q"

            if play_choice in ["S", "J", "R"]:
                return "R"

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
        self.decide_online_tour_players(peer, False)
        print("Waiting for remote list of players...")
        opp_players = peer.receive()  # Sync player lists
        peer.send(self.players)

        for i in opp_players.keys():
            if i in self.players.keys():
                self.players[i + " (opponent)"] = opp_players[i]
            else:
                self.players[i] = opp_players[i]
        peer.receive()  # Block needed here to ensure clients are synced
        t = Tournament(list(self.players.keys()))  # Create tournament
        data = dict()  # Dictionary containing various data needed by remote peer
        data["instruction"] = None  # Instructions in the form of strings
        data["players"] = None  # players to play next game
        data["tour"] = t.get_scoreboard()  # String representing current tournament bracket
        peer.send(data)  # Send initial tournament bracket
        winner = ""

        while True:
            self.graphics.make_header("Tournament Standings")
            data["tour"] = t.get_scoreboard()
            print(data["tour"])
            end = t.winner_state
            players = t.opponents
            mode = self.setup_tournament_game(t)
            winners = []

            if end == 1:  # Completed tournament
                data["instruction"] = "COMPLETE"
                data["player"] = winner
                peer.send(data)
                self.graphics.make_header(winner + " Has won the tournament!")
                peer.teardown()
                break
            else:
                self.graphics.make_header("Up next: Local " + players[0] +
                                          " vs remote " + players[1])
                self.new_game()  # Setup game
                self.play.init_players(mode, self.difficulty, t.opponents[0],
                                       t.opponents[1])
                data["players"] = players
                data["instruction"] = "PLAY"
                data["play"] = self.play
                peer.send(data)

                while True:
                    winner = game.online_vs(players[0], peer, self.players[players[0]], True, self.play)

                    if winner != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")

                if winner == players[0]:  # If local player won
                    winners.append(winner)
                    self.graphics.make_header(winner + " has advanced to the next round!")
                else:  # If remote player won
                    winner = players[1]
                    winners.append(winner)
                    self.graphics.make_header(winner + " has advanced to the next round!")
            t.next_game(winner)

    def client_side_tournament(self):
        """
        The client side of an online tournament game.
        """
        self.server = False
        peer = Peer(False)  # Setup
        peer.connect_to_server()
        self.decide_online_tour_players(peer, True)
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
                self.graphics.make_header(data["player"] + " has won the tournament!")
                peer.teardown()
                break
            elif data["instruction"] == "PLAY":
                players = data["players"]
                self.graphics.make_header("Up next: (local) " + players[1] + " vs (remote) " + players[0])

                while True:
                    winner = game.online_vs(players[1], peer, self.players[players[1]], False, data["play"])

                    if winner != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")

                if winner == players[1]:  # If local player won
                    self.graphics.make_header(winner + " has advanced to the next round!")
                else:  # If remote player won
                    self.graphics.make_header(players[0] + " has advanced to the next round!")
            data = peer.receive()

    # def get_local_names(self):
    #     """
    #     Sig:    None
    #     Pre:    None
    #     Post:   List of names, and list of booleans corresponding to whether player is human or NPC
    #     """
    #     players = [self.player]
    #     humans = []
    #
    #     for i in range(2):
    #         if i:
    #             players.append(input("Name player " + str(i + 1) + ": "))
    #         while True:
    #             human = input("Is this a human player? [" + self.graphics.set_color("G", "Y") + "/" + self.graphics.set_color("R", "N") + "]")
    #             if human == "Y" or human == "y":
    #                 human = True
    #                 break
    #             if human == "n" or human == "n":
    #                 human = False
    #                 break
    #         humans.append(human)
    #     return players, humans
    #
    # def get_online_name(self):
    #     """
    #     Sig:    None
    #     Pre:    None
    #     Post:   Name, and boolean corresponding to whether player is human or NPC
    #     """
    #     while True:
    #         human = input("Are you a human player? [" + self.graphics.set_color("G", "Y") + "/" + self.graphics.set_color("R", "N") + "]")
    #         if human == "Y" or human == "y":
    #             human = True
    #             break
    #         if human == "n" or human == "n":
    #             human = False
    #             break
    #     return self.player, human

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
                    return int(ai_num)
            except:
                continue

    def setup_tournament_players(self):
        """
        Where the number of players are chosen for single player tournament
        """
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

    def setup_player_names(self, user_num, ai_num=0):
        """
        Where user player names are entered and AI names randomly generated
        ALso creates a new Play instance and resets the player and AI names
        :param user_num: the number of user players
        :param ai_num: the number of AI players
        """
        self.players = {self.user: True}

        if self.server:
            self.ai_names = ["Ralph", "Randy", "Roger", "Rhys", "Rooster", "Adam",
                            "Rob", "Ryan", "Richy", "Ross", "Ricky", "Rory", "Maxime"]
        else:
            self.ai_names = ["Viktor", "Peter", "Paul", "Chris", "Charles", "Pelle",
                            "Josh", "Steve", "Michael", "Larry", "Laurin", "Gustav"]

        for i in range(2, int(user_num) - int(ai_num) + 1):
            name = input("Enter a unique player " + str(i) +
                         " name:\n")[:self.NAME_LEN].capitalize()

            while name in self.players.keys():
                name = input("Enter a unique player " + str(i) +
                             " name:\n")[:self.NAME_LEN].capitalize()
            self.players[name] = True
        self.players.update(dict({self.ai_names.pop(self.ai_names.index(choice(
            self.ai_names))): False for j in range(int(ai_num))}.items()))

        if user_num == ai_num:
            self.players.pop(self.user)

    def decide_online_tour_players(self, peer, remote):
        """
        Determines the number of players between host and client users
        :param peer: peer is connected to another peer
        :param remote: remote connection
        """
        while True:
            nr_players = input("How many players on this computer? [" +
                               self.graphics.set_color("G", "1 - 7") + "]\n")
            try:
                if 1 <= int(nr_players) <= 7:
                    nr_players = int(nr_players)
                    break
            except:
                continue
        # Send number of players and ensure remote and local don't exceed 8
        peer.send(nr_players)
        print("Confirming number of players...")
        opp_players = peer.receive()

        if not 3 <= (opp_players + nr_players) <= 8:
            print("Your total is not between 3 and 8. Try again.")
            self.decide_online_tour_players(peer, remote)
        ai_num = self.setup_ai_players(nr_players)
        if ai_num > 0 and self.server:
            self.setup_ai_difficulty(ai_num)
        self.setup_player_names(nr_players, ai_num)

    def close_comms(self):
        """
        Prints a thank you message to the user and closes the program
        """
        self.graphics.make_header("Thanks for playing!")
        exit(1)
