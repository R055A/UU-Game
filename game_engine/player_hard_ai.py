from game_engine.player_ai import PlayerAI


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
        pass

    def minimax(self, position, depth, alpha, beta, maximize):
        if depth == 0:
            if position.has_won_game():
                return position.is_my_turn ? 1 : -1

        if maximize:
            maxEval = -inf
            for possibleMove in position.possibleMoves:
                eval = self.minimax(self, possibleMove, depth-1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha. eval)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = inf
            for possibleMove in position.possibleMoves:
                eval = self.minimax(self, possibleMove, depth-1, alpha, beta, True)
                minEval = max(minEval, eval)
                alpha = max(alpha. eval)
                if beta <= alpha:
                    break
            return minEval
