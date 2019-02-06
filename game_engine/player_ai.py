from game_engine.player_abstract import Player


class PlayerAI(Player):
    """
    AI player abstract class - super class for AI difficulty classes
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 06/02/2019
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the game instance
        :param name: the name of the player
        """
        super().__init__(game, name)

    def characteristic_count(self, pce, y, x, d_y, d_x, dif):
        """
        Counts the similarities found for each characteristic of a
        selected piece in a given direction from a given available
        position on the board for a given number of blocks/difficulty
        :param pce: the selected piece for placing somewhere on the board
        :param y: the row position of the available/empty board cell
        :param x: the column position of the available/empty board cell
        :param d_y: the x-direction being checked for similarities (-1, 0, 1)
        :param d_x: the y-direction being checked for similarities (-1, 0, 1)
        :param dif: the AI difficulty being played; either 1, 2, or 3 for hard
        :return: a list of similarity counts for each characteristic of a piece
        """
        return [len([k for i in range(1, dif + 1) if self.game.board
                [(d_y * i + y) % self.game.N][(d_x * i + x) % self.game.N] and
                self.game.board[(d_y * i + y) % self.game.N][(d_x * i + x) %
                self.game.N][pce.index(k)] == k]) for k in pce]
