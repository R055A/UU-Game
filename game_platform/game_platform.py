#!/usr/bin/env python3

from game_engine.play import Play
from game_platform.game_display import GameDisplay
from game_engine.player_human import PlayerHuman


class GamePlatform:
    """
    The GamePlatform class
    Author(s): Adam Ross
    Last-edit-date: 06/03/2019
    """

    def __init__(self):
        """
        GamePlatform class constructor
        """
        self.play = Play()  # Play class instance
        self.display = GameDisplay(self.play)  # GameDisplay class instance
        self.board = [[i for i in range(j - 4, j)] for j in range(5, 18, 4)]

    def play_local(self):
        """
        Plays a local game between either user vs user, user vs AI, or AI vs AI
        :return: the winner's name or None for a draw
        """
        game_start = True  # Boolean for the start of the game

        while True:
            if game_start:
                self.display.display_game_status()
                game_start = False
            self.select_piece()
            self.place_piece()

            if self.play.game.has_won_game(self.play.selected_piece):
                self.display.display_game_status()
                return self.play.current_player.name
            elif not self.play.game.has_next_play():  # checks if turns remain
                self.display.display_game_status()
                return None

    def online_vs(self, name, peer, server, auto):
        """
        Plays online 1 vs 1 games
        :param name: players name
        :param peer: network connection
        :param server: if player is server host
        :param auto: Boolean for if game is automated or not
        """
        if server:
            if self.play.current_player == name:
                starting_player = True
                peer.send("WAIT")
                peer.receive()
            else:
                starting_player = False
                peer.send("START")
                peer.receive()
        else:
            ack = peer.receive()

            if ack == "WAIT":
                starting_player = False
                peer.send("ACK")
            else:
                starting_player = True
                peer.send("ACK")

        if starting_player:
            return self.play_game(True, True, peer, auto)
        else:
            return self.play_game(False, True, peer, auto)

    def play_game(self, my_turn, first_draw, c, auto):
        while True:
            if not auto:
                self.display.display_game_status()

            if not my_turn:
                if first_draw and not auto:
                    print("\nWait for opponent to pass a piece")
                elif not auto:
                    print("\nWait for opponent to place the piece")
                self.play = c.receive()

                if not auto:
                    self.display.display_game_status()

                if self.play.game.has_won_game(self.play.selected_piece):
                    return self.play.current_player.name
                elif not self.play.game.has_next_play():
                    return "DRAW"

                if not first_draw:
                    if not auto:
                        print("\nWait for opponent to pass a piece")
                    self.play = c.receive()

                    if not auto:
                        self.display.display_game_status()
                first_draw = False
                my_turn = True

            if not first_draw:
                self.place_piece()
                c.send(self.play)

                if self.play.game.has_won_game(self.play.selected_piece):
                    return self.play.current_player.name
                elif not self.play.game.has_next_play():
                    return "DRAW"
            self.select_piece()

            if not auto:
                self.display.display_game_status()

            if first_draw:
                my_turn = False
                first_draw = False
            c.send(self.play)
            my_turn = False

    def place_piece(self):
        """
        Prompts user to select a board place for a piece or auto selects if AI
        """
        if isinstance(self.play.current_player, PlayerHuman):
            self.display.display_game_status()

            while True:
                try:
                    i = input("\nEnter a board number for placing a piece:\n")

                    if 1 <= int(i) <= 16:
                        y, x = [(k, j) for j in range(4) for k in range(4)
                                if self.board[k][j] == int(i)][0]

                        if self.play.play_placement(int(y), int(x)):
                            break
                except:
                    continue
        else:
            self.play.play_placement()

    def select_piece(self):
        """
        Prompts user to select a piece, or auto selects if AI
        """
        if isinstance(self.play.current_player, PlayerHuman):
            self.display.display_game_status()

            while True:
                pce = input("\nEnter a number for the piece being selected:\n")

                if 1 <= int(pce) <= 16:
                    if self.play.play_selection(str(int(pce) - 1)):
                        break
        else:
            self.play.play_selection()
