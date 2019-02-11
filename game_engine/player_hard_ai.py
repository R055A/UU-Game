from game_engine.player_ai import PlayerAI
from game_engine.minimax import Minimax
from random import randint


class PlayerHardAI(PlayerAI):
    """
    The Hard difficulty AI class
    Author(s): Viktor Enzell, Laurin Kerle
    Last-edit-date: 10/02/2019
    """

    def __init__(self, game, name):
        """
        Initialises the class variables
        :param game: the game instance
        :param name: the name of the player
        """
        super().__init__(game, name)
        self.depth = 3  # The depth at which the Minimax algorithm should stop
        self.chosen_piece = None  # The piece chosen by the Minimax algorithm

    def choose_piece(self):
        """
        Method for hard difficulty AI piece choosing
        :return: a random piece if it is the first round
        Otherwise a piece chosen by the Minimax algorithm
        """
        if len(self.game.pieces.keys()) == 16:
            return str(randint(0, 15))
        return str(self.chosen_piece)

    def place_piece(self, selected_piece):
        """
        Method for hard difficulty AI piece placing on board.
        Selects where to place piece and saves piece chosen by Minimax algorithm
        :param selected_piece the piece selected for placing on board
        """
        game_clone = self.game.clone_game()                         # temporary solution since minimax needs the
        game_clone.pieces[int(selected_piece, 2)] = selected_piece  # selected piece still among the pieces

        minimax = Minimax(game_clone, self.depth, int(selected_piece, 2))
        best_move = minimax.get_move()
        self.chosen_piece = best_move.passed_piece
        self.game.place_piece(best_move.spot)
