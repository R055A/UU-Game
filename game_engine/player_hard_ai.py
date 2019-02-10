from game_engine.player_ai import PlayerAI
from game_engine.minimax import Minimax


class PlayerHardAI(PlayerAI):
    """
    The Hard difficulty AI class
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the game instance
        :param name: the name of the player
        """
        super().__init__(game, name)
        self.depth = 3

    def choose_piece(self):
        """
        Method for hard difficulty AI piece choosing
        :return: the selected piece for placing on the board
        """
        pass

    def place_piece(self, selected_piece):
        """
        Method for hard difficulty AI piece placing on board
        :param selected_piece the piece selected for placing on board
        """
        minimax = Minimax(self.game, self.depth)
        best_move = minimax.get_move()

        # place_piece(best_move.get_cell())

        # pass_piece(best_move.get_passed_piece())
