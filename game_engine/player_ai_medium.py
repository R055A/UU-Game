from game_engine.player_ai import PlayerAI


class PlayerMediumAI(PlayerAI):
    """
    The Medium difficulty AI class
    Author(s):      Gustav From; Adam Ross
    Last-edit-date: 06/02/19
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
        Method for medium difficulty AI piece choosing
        :return: the selected piece for placing on the board
        """
        return '1'

    def place_piece(self, selected_piece):
        """
        Method for medium difficulty AI piece placing on board
        :param selected_piece the piece selected for placing on board
        """
        pass
