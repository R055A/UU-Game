from player_abstract import Player


class PlayerHuman(Player):
    """
    The human player class
    Author: Adam Ross
    Date:   30/01/2019
    """

    def __init__(self, game, name):
        super().__init__(game, name)

    def choose_piece(self):
        """
        Prompts user to select a piece for the other player to place on board
        :return: the selected piece
        """
        while True:
            selected_piece = input("\nEnter number 0-15 of piece selection: ")

            if selected_piece in self.game.pieces.keys():  # validate selection
                return selected_piece

    def place_piece(self, selected_piece):
        """
        Prompts user to enter a board cell coords for placing selected piece
        """
        while True:
            x, y = input("\nEnter 2 ints 0 - 3 separated by a space: ").split()

            try:
                if self.is_selected_cell_valid(int(x), int(y)):
                    self.game.board[x][y] = selected_piece
                    break
            except:
                continue