from game_engine.player_ai import PlayerAI


class PlayerEasyAI(PlayerAI):
    """
    The easy difficulty AI class
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
        Method for easy difficulty AI piece choosing
        :return: the selected piece for placing on the board
        """
        return self.get_best(dict({str(pce): self.hard(self.game.pieces[pce])
                                   for pce in self.game.pieces}.items()), False)

    def place_piece(self, selected_piece):
        """
        Method for easy difficulty AI piece placing on board
        :param selected_piece the piece selected for placing on board
        """
        y, x = self.easy(selected_piece)[0]
        self.game.board[y][x] = selected_piece
