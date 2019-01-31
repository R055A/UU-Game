from player_abstract import Player
from random import choice, randint


class PlayerAI(Player):
    """
    AI player abstract class - super class for AI difficulty classes
    Author: Adam Ross
    Date:   30/01/2019
    """

    def __init__(self, game, name):
        super().__init__(game, name)

    def choose_piece(self):
        """
        Temporary AI choose piece method - purely random choice
        Could be abstract when implementing different difficulties
        :return: the selected piece for placing on the board
        """
        return choice(list(self.game.pieces.keys()))

    def place_piece(self, selected_piece):
        """
        Temporary AI place piece on board method - purely random
        Could be abstract when implementing different difficulties
        """
        while True:
            x, y = randint(0, self.game.N - 1), randint(0, self.game.N - 1)

            if self.is_selected_cell_valid(x, y):  # validates selected cell
                self.game.board[x][y] = selected_piece
                break
