from game_engine.game import Game
from game_engine.player_human import PlayerHuman
from game_engine.player_medium_ai import PlayerMediumAI
from random import choice


class Play:
    """
    The game play class
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 06/02/2019
    """

    def __init__(self):
        self.game = Game()  # initiates an instance of the Game class
        self.players = None  # initiates players list
        self.current_player = None  # initiates current player turn
        self.selected_piece = None  # initiates current selected piece

    def play_turn(self):
        """
        Where the game turns are played
        """
        self.game.declare_available_pieces()  # prints game board status
        self.game.declare_board_status()  # prints available pieces status
        self.selected_piece = self.game.pieces.pop(self.current_player.
                                                   choose_piece())
        self.declare_selected_piece()  # prints the selected piece
        self.current_player = self.change_player()  # swaps player turn
        self.declare_current_player()  # prints the current player turn
        self.current_player.place_piece(self.selected_piece)  # places piece

        if self.game.has_won_game():  # checks if game won - not implemented
            pass
        elif not self.game.has_next_play():  # checks if play turns remaining
            self.game.declare_board_status()  # prints final status of board
        else:
            self.play_turn()  # plays the next turn

    def init_players(self, mod, dif=0, p_one="Player One", p_two="Player Two"):
        """
        Initializes the two players for the game dependent on game mode
        """
        if mod == 1:  # if human player vs human player
            self.players = [PlayerHuman(self.game, p_one),
                            PlayerHuman(self.game, p_two)]
        elif mod == 2:  # if human player vs AI player
            if dif == 1:  # if easy difficulty AI
                pass
            elif dif == 2:  # if medium difficulty AI
                self.players = [PlayerHuman(self.game, p_one),
                                PlayerMediumAI(self.game, p_two)]
            else:  # if hard difficulty AI
                pass
        else:  # if AI player vs AI player
            if dif == 1:  # if easy difficulty AI
                pass
            elif dif == 2:  # if medium difficulty AI
                self.players = [PlayerMediumAI(self.game, p_one),
                                PlayerMediumAI(self.game, p_two)]
            else:  # if hard difficulty AI
                pass
        self.current_player = choice(self.players)  # random starting player
        self.declare_current_player()  # prints the starting player turn

    def change_player(self):
        """
        Toggles player selection for when the game play turn changes
        :return: the new selected player for the current game play turn
        """
        return self.players[abs(self.players.index(self.current_player) - 1)]

    def declare_current_player(self):
        """
        Temporary printing of current player for CLI testing and presenting
        """
        print("\nCurrent player is '" + self.current_player.name + "'")

    def declare_selected_piece(self):
        """
        Temporary printing of selected piece for CLI testing and presenting
        """
        print("\nCurrent piece is " + self.selected_piece)
