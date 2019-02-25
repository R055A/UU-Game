#!/usr/bin/env python3

import communication_platform.game as game
import communication_platform.peer as peer
import communication_platform.tournament as tour
from game_engine.play import Play
from communication_platform.graphics import Graphics
from random import choice


class CommunicationPlatform:
    """
    Communication platform main class
    Refactoring/integration editor(s): Adam Ross
    Last-edit-date: 24/02/2019
    """

    def __init__(self):
        """
        Class constructor
        """
        self.graphics = Graphics()
        self.play = None
        self.player = None
        self.ai_names = None
        self.players = None

    def new_game(self):
        """
        Creates a new Play instance for each game played
        """
        self.ai_names = ["Ralph", "Randy", "Roger", "Rhys", "Rooster",
                         "Rob", "Ryan", "Richy", "Ross", "Ricky"]
        self.players = {self.player: True}
        self.play = Play()

    def menu_options(self):
        """
        A menu for selecting single or tournament game play or app termination
        """
        self.graphics.make_header("Welcome to UU-Game!")
        self.player = input("Enter player name: \n")

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
        :param game_mode:
        :return:
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

    def single_player_tournament(self):
        """
        A single-player tournament locally between players
        :return: the resulting play choice for the main menu options
        """
        self.graphics.make_header("Tournament play!")
        player_num, ai_num = self.setup_tournament_players()
        self.setup_player_names(player_num, ai_num)
        return "R"

        # ____________________TO BE REFACTORED_______________________

        # # Play tournament
        # t = tour.Tournament(list(players.keys()))
        #
        # while True:
        #     self.graphics.make_header("Tournament Standings")
        #     print(t.get_scoreboard())
        #     end = t.winner_state
        #     players = t.opponents
        #
        #     if end == 1:  # Last game already played
        #         break
        #     else:
        #         self.graphics.make_header("Up next: " + players[0] +
        #         " vs " + players[1])
        #         humans = [human_dict[players[0]], human_dict[players[1]]]
        #         while True:
        #             winner = game.local_vs(players, humans)
        #             if winner != "DRAW":
        #                 break
        #             else:
        #                 self.graphics.make_header("Draw game! Replaying game")
        #         t.next_game(winner)  # Set winner of current game
        #         self.graphics.make_header(winner +
        #         " has advanced to the next round!")
        #
        # self.graphics.make_header(winner + " has won the tournament!")

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
        c = peer.Peer(True)
        c.accept_client()
        player_list, human_dict = self.decide_online_tour_players(c, False)
        print("Waiting for remote list of players...")

        # Sync player lists
        remote_player_list = c.receive()
        player_list = player_list + remote_player_list
        c.send(player_list)
        remote_human_dict = c.receive()
        human_dict.update(remote_human_dict)
        c.send(human_dict)
        c.receive()  # Block needed here to ensure clients are synced

        # Create tournament and setup instructions
        t = tour.Tournament(player_list)
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
                    winner = game.online_vs(players[0], c, human_dict[players[0]], True)
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
        c = peer.Peer(False)
        c.connect_to_server()
        player_list, human_dict = self.decide_online_tour_players(c, True)

        # Sync player lists
        c.send(player_list)
        player_list = c.receive()
        c.send(human_dict)
        human_dict = c.receive()
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
                    winner = game.online_vs(players[1], c, human_dict[players[1]], False)
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
            ai_num = input("Choose the number of AI players? [" + self.graphics.
                           set_color("G", "0 - " + player_num) + "]\n")

            try:
                if type(int(ai_num)) == int and int(ai_num) <= int(player_num):
                    break
            except:
                continue
        return int(player_num), int(ai_num)

    def setup_player_names(self, player_num, ai_num=0):
        """
        Where user player names are entered and AI names randomly generated
        ALso creates a new Play instance and resets the player and AI names
        """
        self.new_game()

        for i in range(2, int(player_num) - int(ai_num) + 1):  # Name players
            name = input("Enter a unique player " + str(i) + " name:\n")

            while name in self.players.keys():
                name = input("Enter a unique player " + str(i) + " name:\n")
            self.players[name] = True

        for j in range(int(ai_num)):
            self.players[self.ai_names.
                pop(self.ai_names.index(choice(self.ai_names)))] = False

    def decide_online_tour_players(self, c, remote):
        """
        Sig:    Peer ==> array, dictionary
        Pre:    Peer is connected to another peer
        Post:   Array containing list of players on this side of connection, dictionary containing whether \
                players are human or computer controlled
        """
        # Determine number of players
        while True:
            choice = input("How many players on this computer? [" + self.graphics.set_color("G", "1-7") + "](maximum 8 total) ")
            if type(int(choice)) == int:
                choice = int(choice)
                if 1 <= choice <= 7:
                    break

        # Send number of players and ensure remote and local don't exceed 8
        c.send(choice)
        print("Confirming number of players...")
        remote_choice = c.receive()
        if remote_choice + choice > 8:
            print("Your total is over 8. Try again")
            self.decide_online_tour_players(c, remote)

        nr_players = choice
        player_list = []  # Strings of names
        human_dict = {}  # Booleans. Key = player. True = Human, False = NPC
        # Determine names and human/computer controlled
        while True:
            choice = input("How many AI players? [" + self.graphics.set_color("G", "0-" + str(nr_players)) + "] ")
            if type(int(choice)) == int:
                choice = int(choice)
                if choice <= nr_players:
                    break
        nr_ai = choice

        # Name human players
        for player in range(nr_players - nr_ai):
            name = input("Name player" + str(player + 1) + ": ")
            player_list.append(name)
            human_dict[name] = True

        # Name AI players
        names = ["SKYNET", "MAX HEADROOM", "WATSON", "DEEP THOUGHT", "J.A.R.V.I.S.", "R2D2", "MU-TH-UR 6000",
                 "TÄNKANDE AUGUST"]
        for nr in range(nr_ai):
            # This is to ensure that server/client dont create players with the same name
            if remote:
                name = names[nr]
            else:
                name = names[nr + 4]
            player_list.append(name)
            human_dict[name] = False

        return player_list, human_dict

    def closing_message(self):
        self.graphics.make_header("Thanks for playing!")
