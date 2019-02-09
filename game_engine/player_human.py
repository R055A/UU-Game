from game_engine.player_abstract import Player


class PlayerHuman(Player):
    """
    The human player class
    Author(s):      Adam Ross
    Last-edit-date: 08/02/2019
    """

    def __init__(self, game, name):
        super().__init__(game, name)

    def choose_piece(self, slctd_pce=None):
        """
        Selects a piece for the other player to place on board
        -- Temporarily prompts user to enter a value 0-15 for testing --
        :return: the selected piece
        """
        while True:
            slctd_pce = input("\nEnter number 0-15 of piece selection: ")

            if slctd_pce in self.game.pieces.keys():  # validate selection
                return slctd_pce

    def place_piece(self, slctd_pce, y=None, x=None):
        """
        Places a selected piece on the game board
        -- Temporarily prompts user to enter a board position for testing --
        """
        while True:
            try:
                x, y = input("\nEnter 2 ints 0 - 3 separated by a space: ").\
                    split()

                if self.is_cell_empty(int(x), int(y)):
                    self.game.board[int(x)][int(y)] = slctd_pce
                    break
            except:
                continue
