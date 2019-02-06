class Game:
    """
    Game entity class
    Author(s):      Adam Ross
    Last-edit-date: 06/02/2019
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
        return True in ([len([[k for k in self.board[i][i] if k == self.board
                [i][j][self.board[i][i].index(k)]] for j in range(self.N) if i
                != j and self.board[i][j]]) == 3 or len([[k for k in self.board
                [i][i] if k == self.board[j][i][self.board[i][i].index(k)]] for
                j in range(self.N) if i != j and self.board[j][i]]) == 3 for i
                in range(self.N) if self.board[i][i]]) or len([[k for k in
                self.board[0][0] if k == self.board[0 + i][0 + i][self.board[0]
                [0].index(k)] and self.board[0][0]] for i in range(self.N) if
                self.board[i][i] and i != 0]) == 3 or len([[k for k in self.
                board[0][3] if k == self.board[i][(i + i + 3) % 3][self.board
                [0][3].index(k)] and self.board[i][(i + i + 3) % 3]] for i in
                range(self.N) if self.board[i][(i + i + 3) % 3] and i != 0]) == 3

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
