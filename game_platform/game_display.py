#!/usr/bin/env python3

from os import system
from game_platform.piece import Piece
from util.graphics import Graphics
from game_engine.player_human import PlayerHuman
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_medium import PlayerMediumAI


class GameDisplay:
    """
    The GameDisplay class
    Author(s): Adam Ross
    Last-edit-date: 06/03/2019
    """

    SELECTING = "selecting"
    PLACING = "placing"
    HARD = "AI - hard"
    MEDIUM = "AI - medium"
    EASY = "AI - easy"

    def __init__(self, play):
        """
        GamePlatform class constructor
        :param play: instance of the Play() class
        """
        self.play = play  # Play class instance
        self.graphics = Graphics()  # Graphics class instance
        self.players = None  # the two players playing a game
        self.piece_pool = None  # the pool of sixteen pieces
        self.pce = None  # the selected piece in game play

    def display_game_status(self):
        """
        Displays the current game status of the players, board and piece pool
        """
        system('clear')
        self.display_game_header()
        self.display_piece_pool()
        self.display_board()

    def display_game_header(self):
        """
        Displays the players names, if AI with difficulty, and players turn
        """
        self.players = self.play.players
        p_o, p_t = (self.graphics.set_color("P", i.name) for i in self.players)
        dsp = "#" * 83 + "\n#" + " " * ((40 - len(self.players[0].name)) // 2)\
              + p_o + " " * ((40 - len(self.players[0].name)) // 2)
        dsp += "|" if (40 - len(self.players[0].name)) % 2 == 0 else " |"
        dsp += " " * ((40 - len(self.players[1].name)) // 2) + p_t +\
               " " * ((40 - len(self.players[1].name)) // 2)
        dsp += "#\n" if (40 - len(self.players[1].name)) % 2 == 0 else " #\n"
        dsp += "#" + "-" * 81 + "#\n#"

        if isinstance(self.players[0], PlayerHuman):
            if self.players[0].name == self.play.current_player.name:
                if self.has_selected_piece():
                    p_o = self.graphics.set_color("G", self.PLACING)
                    p_o_len = len(self.PLACING)
                else:
                    p_o = self.graphics.set_color("G", self.SELECTING)
                    p_o_len = len(self.SELECTING)
            else:
                p_o = " "
                p_o_len = 1
        elif isinstance(self.players[0], PlayerEasyAI):
            p_o = self.EASY
            p_o_len = len(self.EASY)
        elif isinstance(self.players[0], PlayerMediumAI):
            p_o = self.MEDIUM
            p_o_len = len(self.MEDIUM)
        else:
            p_o = self.HARD
            p_o_len = len(self.HARD)

        if isinstance(self.players[1], PlayerHuman):
            if self.players[1].name == self.play.current_player.name:
                if self.has_selected_piece():
                    p_t = self.graphics.set_color("G", self.PLACING)
                    p_t_len = len(self.PLACING)
                else:
                    p_t = self.graphics.set_color("G", self.SELECTING)
                    p_t_len = len(self.SELECTING)
            else:
                p_t = " "
                p_t_len = 1
        elif isinstance(self.players[1], PlayerEasyAI):
            p_t = self.EASY
            p_t_len = len(self.EASY)
        elif isinstance(self.players[1], PlayerMediumAI):
            p_t = self.MEDIUM
            p_t_len = len(self.MEDIUM)
        else:
            p_t = self.HARD
            p_t_len = len(self.HARD)
        dsp += " " * ((40 - p_o_len) // 2) + p_o + " " *\
               ((40 - p_o_len) // 2)
        dsp += "|" if (40 - p_o_len) % 2 == 0 else " |"
        dsp += " " * ((40 - p_t_len) // 2) + p_t + " " *\
               ((40 - p_t_len) // 2)
        dsp += "#\n" if (40 - p_t_len) % 2 == 0 else " #\n"
        print(dsp + "#" * 83)

    def display_piece_pool(self):
        """
        Displays the piece pool and selected piece in the game status display
        """
        self.piece_pool = dict({i: Piece(self.play.game.pieces[i]) for i in
                                self.play.game.pieces}.items())
        dsp = "#" + "-" * 81 + "#\n#|"

        for i in range(8):
            dsp += "  " + str(i + 1) + ": " + self.piece_pool[str(i)].\
                get_chars() + " |" if str(i) in self.piece_pool.keys() \
                else "  " + str(i + 1) + ":     " + "|"
        dsp += "#\n#|  9: " + self.piece_pool['8'].get_chars() +\
               " |" if '8' in self.piece_pool.keys() else "#\n#|  9:     |"

        for i in range(9, 16):
            dsp += " " + str(i + 1) + ": " + self.piece_pool[str(i)].\
                get_chars() + " |" if str(i) in self.piece_pool.keys() \
                else " " + str(i + 1) + ":     " + "|"
        dsp += "#\n#" + "-" * 81

        if self.has_selected_piece():
            dsp += "#\n#" + " " * 31 + "Selected Piece: " + self.pce + " " * 31
        print(dsp + "#\n" + "#" * 83)

    def has_selected_piece(self):
        """
        Checks if there is a selected piece not yet placed on the board
        :return: the selected piece if it if not on board, None otherwise
        """
        if self.play.selected_piece and \
                len([r for r in self.play.game.board if
                     self.play.selected_piece in r]) == 0:
            self.pce = Piece(self.play.selected_piece).get_chars()
        else:
            self.pce = None
        return self.pce

    def display_board(self):
        """
        Displays the current state of the board in the game status display
        ---------- Temporary until a real version is completed ----------
        """
        print("\nGame board status:")
        print(*(row for row in self.play.game.board), sep="\n")