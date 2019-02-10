from abc import abstractmethod


class Player:
    """
    Abstract super class for human and AI players
    Author(s):      Adam Ross
    Last-edit-date: 09/02/2019
    """

    def __init__(self, game, name):
        """
        Player class constructor
        :param game: the Game class instance
        :param name: the player's name
        """
        self.game = game  # an instance of the Game class
        self.name = name  # a name to define each player

    @abstractmethod
    def choose_piece(self):
        """
        Abstract method for selecting a piece from available group of pieces
        :return: the selected piece
        """

    @abstractmethod
    def place_piece(self, selected_piece):
        """
        Abstract method for selecting a cell on the board for placing piece
        :param selected_piece: the selected piece
        """

    def is_cell_empty(self, x, y):
        """
        Validates that the selected cell is available for placing a piece
        :return: true if the selected cell is empty, false otherwise
        """
        return not self.game.board[x][y]  # checks if a board cell is empty
