from game_platform.piece import Piece


class GamePlatform:
    """
    The GamePlatform class
    Author(s): Adam Ross
    Last-edit-date: 28/02/2019
    """

    def __init__(self, play):
        """
        GamePlatform class constructor
        :param play: instance of the Play() class
        """
        self.play = play
        self.piece_pool = self.update_piece_pool()
        self.board = self.update_board()
        self.add_selected_piece()

    def update_piece_pool(self):
        """
        Updates the piece pool from the Game class instance
        :return: dictionary containing pieces in piece pool with imagery
        """
        return dict({i: Piece(self.play.game.pieces[i]) for i in self.play.
                    game.pieces}.items())

    def update_board(self):
        """
        Updates the board from the Game class instance
        :return: list of lists with played pieces, or None for items
        """
        return self.play.game.board

    def add_selected_piece(self):
        """
        Checks if the selected piece is not on board and adds to piece pool
        """
        if len([r for r in self.board if self.play.selected_piece in r]) == 0:
            self.piece_pool[str(int(self.play.selected_piece, 2))] = \
                Piece(self.play.selected_piece)
