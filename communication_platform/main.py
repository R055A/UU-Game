#!/usr/bin/env python3

import communication_platform.game as game
import communication_platform.peer as peer
from communication_platform.tournament import Tournament
from game_engine.play import Play
from game_engine.player_human import PlayerHuman
from communication_platform.graphics import Graphics
from random import choice
from sys import exit

NAME_LENGTH = 20  # the maximum length of a player's name


class CommunicationPlatform:
    """
    Communication platform main class
    Refactoring/integration editor(s): Adam Ross; Viktor Enzell; Gustav From;
                                       Pelle Ingvast
    Last-edit-date: 27/02/2019
    """

    def __init__(self):
        """
        Class constructor
        """
        self.graphics = Graphics()  # Graphics class instance
        self.play = None  # Play class instance - updated each game play
        self.player = None  # the name of the user
        self.ai_names = None  # the names of each available fictional AI player
        self.players = None  # dictionary for the player names and if users
        self.user = None  # the user name
        self.online = False  # Boolean for in playing multi-player online
        self.difficulty = 0  # the AI game play difficulty; 0; 1 - 3
        self.server = False

    def new_game(self):
        """
        Creates a new Play instance for each game played by a user
        """
        self.play = Play()

    def start_comms(self):
        """
        A menu for selecting single or tournament game play or app termination
        """
        self.graphics.make_header("Welcome to UU-Game!")
        self.user = input("Enter player name: \n")[:NAME_LENGTH].capitalize()

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
                        self.local_vs()

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
                        self.online_vs()

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

    def local_vs(self):
        """
        Sig:    None
        Pre:    None
        Post:   A game played between between two players
        """
        players, humans = self.get_local_names()
        while True:
            result = game.local_vs(players, humans)
            if result != "DRAW":
                break
            else:
                g.make_header("Game draw! Replay game")
        self.graphics.make_header(result + " has won!")

    def online_vs(self):
        """
        Sig:    None
        Pre:    None
        Post:   A game played between against a remote player
        """
        while True:
            name, human = self.get_online_name()
            choice = input("Are you the first to start the game? [" + self.graphics.set_color("G", "Y") + "]es [" \
                           + self.graphics.set_color("R", "N") + "]no\n[" + self.graphics.set_color("R", "Q") + "]uit ")
            if choice == "Y" or choice == "y":
                # Create peer which will act as server
                c = peer.Peer(True)
                c.accept_client()
                while True:
                    # Name, peer, Human, Server
                    win = game.online_vs(name, c, human, True)
                    if win != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")
                if win == name:
                    self.graphics.make_header("You've won!")
                else:
                    self.graphics.make_header("You've lost!")
                c.teardown()
                break

            elif choice == "N" or choice == "n":
                # Create peer which will act as client
                c = peer.Peer(False)
                c.connect_to_server()
                while True:
                    # Name, peer, Human, Server
                    win = game.online_vs(name, c, human, False)
                    if win != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")
                # Name, peer, Human = True, Server = False
                if win == name:
                    self.graphics.make_header("You've won!")
                else:
                    self.graphics.make_header("You've lost!")
                c.teardown()
                break

            elif choice == "Q" or choice == "q":
                break

            else:
                print("Invalid choice, try again")

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
        else:
            self.play_manual()  # plays the next turn

    def single_player_tournament(self):
        """
        A single-player tournament locally between players
        :return: the "Return" play choice for returning to the main menu option
        """
        self.graphics.make_header("Single Player Tournament!")
        player_num, ai_num = self.setup_tournament_players()
        self.setup_player_names(player_num, ai_num)

        if ai_num == player_num:
            self.players.pop(self.user)
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
                    self.declare_current_player()  # TEMPORARY UNTIL WE HAVE A GAME PLATFORM ---------------------------------

                    if mode == 3:
                        if self.play.play_auto():
                            break
                    elif self.play_manual():
                        break
                    else:
                        self.graphics.make_header("Draw game! Replaying game")
                tournament.next_game(self.play.current_player.name)  # Set winner
                self.graphics.make_header(self.play.current_player.name +
                                          " has advanced to the next round!")
        self.graphics.make_header(self.play.current_player.name +
                                  " has won the tournament!")
        return "R"

    def multiplayer_tournament(self):
        """
        A multi-player tournament played remotely between players
        :return: the resulting play choice for the main menu options
        """
        self.graphics.make_header("Tournament play!")

        while True:
            print("Choose from one of the following " + self.graphics.
                  set_color("Y", "multi-player") + " options:\n    [" +
                  self.graphics.set_color("G", "S") + "] - Start a new game\n"
                  "    [" + self.graphics.set_color("G", "J") + "] - Join "
                  "existing game\n    [" + self.graphics.set_color("G", "R") +
                  "] - Return to main menu\n    [" + self.graphics.
                  set_color("R", "Q") + "] - Quit")
            play_choice = input("Enter your " + self.graphics.
                                set_color("G", "choice: \n")).upper()

            if play_choice == "S":
                self.server_side_tournament()  # yet to integrate/refactor

            elif play_choice == "J":
                self.client_side_tournament()  # yet to integrate/refactor

            elif play_choice == "Q":
                return "Q"

            if play_choice in ["S", "J", "R"]:
                return "R"

    def server_side_tournament(self):
        """
        Sig:    None
        Pre:    None
        Post:   A tournament played between local, and remote players. And termination of program

        Notes
        -----
        If multiple messages are sent in a row without being received, they will be concatenated in the pipeline \
        and the receiving end will be unable to process the message. Therefor it is sometime needed to send \
        junk messages to sync the clients
        """
        # Setup
        self.server = True
        c = peer.Peer(True)
        c.accept_client()
        self.decide_online_tour_players(c, False)
        print("Waiting for remote list of players...")
        # Sync player lists
        opp_user = c.receive()

        if opp_user in self.players.keys():
            if self.players[opp_user]:
                self.players[opp_user + " (User)"] = True
            else:
                self.players[self.ai_names.pop()] = False
        c.send(self.user)
        self.players.update(c.receive())
        c.send(self.players)
        c.receive()  # Block needed here to ensure clients are synced
        # Create tournament and setup instructions
        t = Tournament(self.players)
        data = dict()  # Dictionary containing various data needed by remote peer
        data["instruction"] = None  # Instructions in the form of strings
        data["players"] = None  # players to play next game
        data["tour"] = t.get_scoreboard()  # String representing current tournament bracket
        c.send(data)  # Send initial tournament bracket
        winner = ""

        while True:
            self.graphics.make_header("Tournament Standings")
            data["tour"] = t.get_scoreboard()
            print(data["tour"])
            end = t.winner_state
            players = t.opponents
            winners = []

            # Completed tournament
            if end == 1:
                data["instruction"] = "COMPLETE"
                data["player"] = winner
                c.send(data)
                self.graphics.make_header(winner + " Has won the tournament!")
                c.teardown()
                break
            else:
                # Setup game
                self.graphics.make_header("Up next: Local " + players[0] + " vs remote " + players[1])
                data["players"] = players
                data["instruction"] = "PLAY"
                c.send(data)

                while True:
                    winner = game.online_vs(players[0], c, self.players[players[0]], True)
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
        Sig:    None
        Pre:    None
        Post:   A tournament played between local, and remote players. And termination of program
        """
        # Setup
        self.server = False
        c = peer.Peer(False)
        c.connect_to_server()
        self.decide_online_tour_players(c, True)

        print("working")

        # Sync player lists
        c.send(self.user)
        opp_user = c.receive()

        if opp_user in self.players.keys():
            if self.players[opp_user]:
                self.players[opp_user + " (User)"] = True
            else:
                self.players[self.ai_names.pop()] = False
        c.send(self.players)
        self.players.update(c.receive())
        c.send("ACK")  # Sync with remote
        data = c.receive()  # Get initial tournament bracket

        while True:
            self.graphics.make_header("Tournament Standings")
            print(data["tour"])

            # End tournament
            if data["instruction"] == "COMPLETE":
                self.graphics.make_header(data["player"] + " has won the tournament!")
                c.teardown()
                break
            elif data["instruction"] == "PLAY":
                players = data["players"]
                self.graphics.make_header("Up next: Local " + players[1] + " vs remote " + players[0])
                while True:
                    winner = game.online_vs(players[1], c, self.players[players[1]], False)
                    if winner != "DRAW":
                        break
                    else:
                        self.graphics.make_header("Game draw! Replay game")

                if winner == players[1]:  # If local player won
                    self.graphics.make_header(winner + " has advanced to the next round!")
                else:  # If remote player won
                    self.graphics.make_header(players[0] + " has advanced to the next round!")
            data = c.receive()

    def get_local_names(self):
        """
        Sig:    None
        Pre:    None
        Post:   List of names, and list of booleans corresponding to whether player is human or NPC
        """
        players = [self.player]
        humans = []

        for i in range(2):
            if i:
                players.append(input("Name player " + str(i + 1) + ": "))
            while True:
                human = input("Is this a human player? [" + self.graphics.set_color("G", "Y") + "/" + self.graphics.set_color("R", "N") + "]")
                if human == "Y" or human == "y":
                    human = True
                    break
                if human == "n" or human == "n":
                    human = False
                    break
            humans.append(human)
        return players, humans

    def get_online_name(self):
        """
        Sig:    None
        Pre:    None
        Post:   Name, and boolean corresponding to whether player is human or NPC
        """
        while True:
            human = input("Are you a human player? [" + self.graphics.set_color("G", "Y") + "/" + self.graphics.set_color("R", "N") + "]")
            if human == "Y" or human == "y":
                human = True
                break
            if human == "n" or human == "n":
                human = False
                break
        return self.player, human

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

    def setup_tournament_players(self):
        """
        Where the number of players are chosen and player names are entered
        :return: the user and AI player numbers
        """
        while True:  # Decide number of players
            player_num = input("Choose the number of tournament players? [" +
                               self.graphics.set_color("G", "3 - 8") + "]\n")

            try:
                if type(int(player_num)) == int and 2 < int(player_num) < 9:
                    break
            except:
                continue

        while True:  # Decide number of AI players
            ai_num = input("Choose the number of AI players? [" + self.
                           graphics.set_color("G", "0 - " + player_num) +
                           "]\n")

            try:
                if 0 <= int(ai_num) <= int(player_num):
                    break
            except:
                continue

        if int(ai_num) > 0:
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
        return int(player_num), int(ai_num)

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
                         " name:\n")[:NAME_LENGTH].capitalize()

            while name in self.players.keys():
                name = input("Enter a unique player " + str(i) +
                             " name:\n")[:NAME_LENGTH].capitalize()
            self.players[name] = True
        self.players.update(dict({self.ai_names.pop(self.ai_names.index(choice(
            self.ai_names))): False for j in range(int(ai_num))}.items()))

    def decide_online_tour_players(self, c, remote):
        """
        Sig:    Peer ==> array, dictionary
        Pre:    Peer is connected to another peer
        Post:   Array containing list of players on this side of connection, dictionary containing whether \
                players are human or computer controlled
        """
        # Determine number of players
        while True:
            nr_players = input("How many players on this computer? [" +
                               self.graphics.set_color("G", "1 - 8") + "]\n")
            try:
                if 1 <= int(nr_players) <= 8:
                    nr_players = int(nr_players)
                    break
            except:
                continue
        # Send number of players and ensure remote and local don't exceed 8
        c.send(nr_players)
        print("Confirming number of players...")

        if not 3 <= (c.receive() + nr_players) <= 8:
            print("Your total is not between 3 and 8. Try again.")
            self.decide_online_tour_players(c, remote)

        # Determine names and human/computer controlled
        while True:
            nr_ai = input("How many AI players? [" + self.graphics.
                          set_color("G", "0-" + str(nr_players)) + "]\n")

            try:
                if 0 <= int(nr_ai) <= nr_players:
                    nr_ai = int(nr_ai)
                    break
            except:
                continue
        self.setup_player_names(nr_players - nr_ai, nr_ai)

    def close_comms(self):
        self.graphics.make_header("Thanks for playing!")
        exit(1)
