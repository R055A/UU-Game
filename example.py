from random import choice, randint


class GameEngine:
    """
    Game Engine class example for Team-B members
    Author: Adam Ross
    Date:   29/01/2019
    """

    N = 4  # constant for the n * n size of the board

    def __init__(self, player_one, player_two):
        """
        Initializes the game board and the sixteen unique game pieces with four binary characteristics
        Initializes to None further necessary variables that will be implemented globally in the class
        """
        self.pieces = dict({str(i): bin(i)[2:].zfill(self.N) for i in range(self.N * self.N)}.items())
        self.board = [[None for i in range(self.N)] for j in range(self.N)]
        self.players = [player_one, player_two]  # will have selected Player class instances (human or AI)
        self.current_player = choice(self.players)  # randomly selects the starting player
        self.selected_piece = None

    def change_player(self):
        """
        Toggles player selection for when the game play turn changes
        :return: the new selected player
        """
        return self.players[abs(self.players.index(self.current_player) - 1)]

    def example(self):
        """
        Prints initialized game pieces, board, players, and current player
        Simulates a selected piece being placed on the board and player turn change
        Prints the remaining game pieces and the new game board state
        """
        print(self.pieces)
        print(self.board)
        print(self.players)
        print(self.current_player)
        self.selected_piece = choice(list(self.pieces.keys()))  # randomly selects a game piece
        print(self.pieces[self.selected_piece])
        self.board[randint(0, self.N - 1)][randint(0, self.N - 1)] = self.pieces[self.selected_piece]  # adds selected piece to random board cell
        self.pieces.pop(self.selected_piece)  # removes selected piece from available pieces for further selecting
        print(self.pieces)
        print(self.board)
        self.current_player = self.change_player()  # changes the current player to the other player
        print(self.current_player)


game = GameEngine("Human", "AI")  # creates an instance of the game engine class for a human player vs AI player game
game.example()
