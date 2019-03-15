#!/usr/bin/env python3

from game_engine.game import Game
from game_engine.player_human import PlayerHuman
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_medium import PlayerMediumAI
from game_engine.player_ai_hard import PlayerHardAI
from random import choice


class GameEngine:
    """
    The GameEngine class
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 14/02/2019
    """

    def __init__(self):
        """
        The Play class constructor
        """
        self.game = Game()  # initiates a Game class instance
        self.players = []  # a list for players to be added to when initialised
        self.current_player = None  # initiates current player during game play
        self.selected_piece = None  # initiates current selected piece

    def play_selection(self, pce=None):
        """
        The selecting of a piece part of a game turn and
        swapping of current player after a piece is selected
        :param pce: the piece being selected for placing on the board
        """
        if isinstance(self.current_player, PlayerHuman):
            self.selected_piece = self.current_player.choose_piece(pce)

            if self.selected_piece:
                self.selected_piece = self.game.pieces.pop(self.selected_piece)
        else:
            self.selected_piece = self.game.pieces.pop(self.current_player.
                                                       choose_piece())
        if self.selected_piece:
            self.current_player = self.change_player()  # swaps player turn
        return self.selected_piece

    def play_placement(self, y=None, x=None):
        """
        The placing of a selected piece on the board part of a game turn
        :param y: the board row position the piece is being placed for human
        :param x: the board column position the piece is being placed for human
        """
        if isinstance(self.current_player, PlayerHuman):
            return self.current_player.place_piece(self.selected_piece, y, x)
        else:
            self.current_player.place_piece(self.selected_piece)  # place piece

    def init_players(self, players):
        """
        Initializes the two players for the game dependent on game mode
        :param players: dict for the name, type and difficulty for each player
        """
        for i in players:
            if players[i][0]:
                self.players.append(PlayerHuman(self.game, i))
            elif players[i][1] == 1:
                self.players.append(PlayerEasyAI(self.game, i))
            elif players[i][1] == 2:
                self.players.append(PlayerMediumAI(self.game, i))
            else:
                self.players.append(PlayerHardAI(self.game, i))
        self.current_player = choice(self.players)  # random starting player

    def change_player(self):
        """
        Toggles player selection for when the game play turn changes
        :return: the new selected player for the current game play turn
        """
        return self.players[abs(self.players.index(self.current_player) - 1)]
