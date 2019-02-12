from game_engine.player_abstract import Player


class PlayerHuman(Player):
    """
    The human player class
    Author(s):      Adam Ross
    Last-edit-date: 09/02/2019
    """

    def __init__(self, game, name):
        """
        The PlayerHuman class constructor
        :param game: the Game class instance
        :param name: the player's name
        """
        super().__init__(game, name)

    def choose_piece(self, slctd_pce=None):
        """
        Selects and validates a piece for the other player to place on board
        :param slctd_pce: the piece being selected for placing on the board
        -- Temporarily prompts user to enter a value 0-15 for testing --
        :return: the validated selected piece
        """
        while True:
            slctd_pce = input("\nEnter number 0-15 of piece selection: ")

            if slctd_pce in self.game.pieces.keys():  # validate selection
                return slctd_pce

    def place_piece(self, slctd_pce, y=None, x=None):
        """
        Places a selected piece on the game board
        -- Temporarily prompts user to enter a board position for testing --
        :param slctd_pce: the piece selected for placing on the board
        :param y: the row position of the board the piece is being placed
        :param x: the column position of the board the piece is being placed
        """
        while True:
            try:
                x, y = input("\nEnter 2 ints 0 - 3 separated by a space: ").\
                    split()

                if self.game.is_cell_empty(int(x), int(y)):
                    self.game.board[int(x)][int(y)] = slctd_pce
                    break
            except:
                continue
