from game_engine.player_abstract import Player
from abc import abstractmethod


class PlayerAI(Player):
    """
    AI player abstract class - super class for AI difficulty classes
    Author(s):      Adam Ross
    Last-edit-date: 04/02/2019
    """

    def __init__(self, game, name):
        super().__init__(game, name)

    @abstractmethod
    def choose_piece(self):
        """
        Abstract method for different difficulty AI piece choosing
        :return: the selected piece for placing on the board
        """

    @abstractmethod
    def place_piece(self, selected_piece):
        """
        Abstract method for different difficulty AI piece placing on board
        :param selected_piece the piece selected for placing on board
        """
