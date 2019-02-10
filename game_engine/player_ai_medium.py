from game_engine.player_ai import PlayerAI
from random import choice


class PlayerMediumAI(PlayerAI):
    """
    The Medium difficulty AI class
    Author(s):      Gustav From; Adam Ross
    Last-edit-date: 10/02/19
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    def choose_piece(self):
        """
        Method for medium difficulty AI piece choosing
        :return: the selected piece for placing on the board
        """
        return choice([i for i in self.game.pieces.keys()])

    def place_piece(self, slctd_pce):
        """
        Method for medium difficulty AI piece placing on board
        :param slctd_pce the piece selected for placing on board
        """
        move = choice([self.hard(slctd_pce), self.easy(slctd_pce)])

        while not move:
            move = choice([self.hard(slctd_pce), self.easy(slctd_pce)])
        print(move)
        y, x = move[0]
        self.game.board[y][x] = slctd_pce
