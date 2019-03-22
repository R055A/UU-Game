#!/usr/bin/env python3

from game_engine.game_engine import GameEngine
from game_platform.game_display import GameDisplay
from game_engine.player_human import PlayerHuman


class GamePlatform:
    """
    The GamePlatform class
    Author(s): Adam Ross
    Last-edit-date: 21/03/2019
    """

    def __init__(self, header):
        """
        GamePlatform class constructor
        :param header: a header for displaying above the game state
        """
        self.play = GameEngine()  # Play class instance
        self.display = GameDisplay(header)  # GameDisplay class instance
        self.board = [[i for i in range(j - 4, j)] for j in range(5, 18, 4)]

    def play_local(self, auto):
        """
        Plays a local game between either user vs user, user vs AI, or AI vs AI
        :param auto: Boolean for if the game is entirely automated AI vs AI
        :return: the winner's name or None for a draw
        """
        game_start = True  # Boolean for the start of the game

        while True:
            if game_start:
                if not auto:
                    self.display.display_game_status(self.play)
                game_start = False
            self.select_piece()  # player selects a piece for other player
            self.place_piece()  # other player places selected piece on board

            if self.play.game.has_won_game(self.play.selected_piece):
                self.display.display_game_status(self.play)
                return self.play.current_player.name
            elif not self.play.game.has_next_play():  # checks if turns remain
                self.display.display_game_status(self.play)
                return None

    def play_online(self, name, conn, auto):
        """
        Plays an online game between user vs user, user vs AI, or AI vs AI
        :param name: players name
        :param conn: network connection
        :param auto: Boolean for if game is automated or not
        """
        game_start = True  # Boolean for the start of the game

        while True:
            if game_start:
                if not auto:
                    self.display.display_game_status(self.play)
                game_start = False

            if self.play.current_player.name == name:
                self.select_piece()  # player selects a piece for other player
                conn.send(self.play)
            else:
                if not auto:
                    print("Waiting for opponent to select a piece...")
                self.play = conn.receive()

            if self.play.current_player.name == name:
                self.place_piece()  # other player places piece on board
                conn.send(self.play)
            else:
                if not auto:
                    print("Waiting for opponent to place piece on board...")
                self.play = conn.receive()

            if self.play.game.has_won_game(self.play.selected_piece):
                self.display.display_game_status(self.play)
                return self.play.current_player.name
            elif not self.play.game.has_next_play():  # checks if turns remain
                self.display.display_game_status(self.play)
                return None

    def place_piece(self):
        """
        Prompts user to select a board place for a piece or auto selects if AI
        """
        if isinstance(self.play.current_player, PlayerHuman):
            self.display.display_game_status(self.play)

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
            self.display.display_game_status(self.play)

            while True:
                pce = input("\nEnter a number for the piece being selected:\n")

                if 1 <= int(pce) <= 16:
                    if self.play.play_selection(str(int(pce) - 1)):
                        break
        else:
            self.play.play_selection()
