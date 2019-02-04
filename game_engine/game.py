class Game:
    """
    Game Engine entity class
    Author(s):      Adam Ross
    Last-edit-date: 04/02/2019
    """

    N = 4  # constant for n in the n * n size of the board

    def __init__(self):
        """
        Inits a 4x4 board and 16 unique pieces with 4-binary characteristics
        """
        self.pieces = dict({str(i): bin(i)[2:].zfill(self.N)
                            for i in range(2**self.N)}.items())
        self.board = [[None for i in range(self.N)] for j in range(self.N)]

    def has_won_game(self):
        """
        Checks if 4 pieces in a row on the board have similar characteristics
        :return: true if there are 4 similar pieces in a row, false otherwise
        """
        pass  # To do

    def has_next_play(self):
        """
        Checks that there are game pieces available for game play to continue
        :return: true if there are pieces available, false otherwise
        """
        return len(self.pieces) != 0

    def declare_available_pieces(self):
        """
        Declares to the players the pieces available for selection
        Currently prints the available pieces for the CLI testing
        """
        print("\nGame pieces status:")
        print(list(self.pieces.items())[:int((len(self.pieces) + 1) / 2)])

        if len(self.pieces) > 1:
            print(list(self.pieces.items())[int((len(self.pieces) + 1) / 2):])

    def declare_board_status(self):
        """
        Declares to the players the current status of the game board
        Currently prints the board status for the CLI testing
        """
        print("\nGame board status:")
        print(*(row for row in self.board), sep="\n")
