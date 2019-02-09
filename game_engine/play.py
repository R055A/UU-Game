from game_engine.game import Game
from game_engine.player_human import PlayerHuman
from game_engine.player_ai_medium import PlayerMediumAI
from random import choice


class Play:
    """
    The game play class
    Author(s):      Adam Ross; Gustav From
    Last-edit-date: 08/02/2019
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
        self.selected_piece = self.game.pieces.pop(self.current_player.
                                                   choose_piece())
        self.current_player = self.change_player()  # swaps player turn
        self.current_player.place_piece(self.selected_piece)  # places piece

    def init_players(self, mod, dif, p_one="Player One", p_two="Player Two"):
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

    def change_player(self):
        """
        Toggles player selection for when the game play turn changes
        :return: the new selected player for the current game play turn
        """
        return self.players[abs(self.players.index(self.current_player) - 1)]
