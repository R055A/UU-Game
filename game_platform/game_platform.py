from game_platform.piece import Piece
from communication_platform.graphics import Graphics
from game_engine.player_human import PlayerHuman
from game_engine.player_ai_easy import PlayerEasyAI
from game_engine.player_ai_medium import PlayerMediumAI


class GamePlatform:
    """
    The GamePlatform class
    Author(s): Adam Ross
    Last-edit-date: 05/03/2019
    """

    SELECTING = "selecting"
    PLACING = "placing"
    HARD = "AI - hard"
    MEDIUM = "AI - medium"
    EASY = "AI - easy"

    def __init__(self, play):
        """
        GamePlatform class constructor
        :param play: instance of the Play() class
        """
        self.play = play
        self.graphics = Graphics()
        self.players = None
        self.piece_pool = None
        self.selected_piece = None

    def display_game_status(self):
        """
        Displays the current game status of the players, board and piece pool
        """
        self.display_game_header()
        self.display_piece_pool()

    def display_game_header(self):
        """
        Displays the players names, if AI with difficulty, and players turn
        """
        self.players = self.play.players
        dsp = "##################################################" \
              "#################################\n#|"
        dsp += " " * ((39 - len(self.players[0].name)) // 2) + self.players[0].\
            name + " " * ((39 - len(self.players[0].name)) // 2)
        dsp += "|" if len(self.players[0].name) % 2 == 1 else " |"
        dsp += " " * ((39 - len(self.players[1].name)) // 2) + self.players[1].\
            name + " " * ((39 - len(self.players[1].name)) // 2)
        dsp += "|#\n" if len(self.players[0].name) % 2 == 1 else " |#\n"
        dsp += "#----------------------------------------------------------" \
               "-----------------------#\n#|"

        if isinstance(self.players[0], PlayerHuman):
            if self.players[0].name == self.play.current_player.name:
                if self.has_selected_piece():
                    player_one = self.graphics.set_color("G", self.PLACING)
                    player_one_len = len(self.PLACING)
                else:
                    player_one = self.graphics.set_color("G", self.SELECTING)
                    player_one_len = len(self.SELECTING)
            else:
                player_one = " "
                player_one_len = 1
        elif isinstance(self.players[0], PlayerEasyAI):
            player_one = self.EASY
            player_one_len = len(self.EASY)
        elif isinstance(self.players[0], PlayerMediumAI):
            player_one = self.MEDIUM
            player_one_len = len(self.MEDIUM)
        else:
            player_one = self.HARD
            player_one_len = len(self.HARD)

        if isinstance(self.players[1], PlayerHuman):
            if self.players[1].name == self.play.current_player.name:
                if self.has_selected_piece():
                    player_two = self.graphics.set_color("G", self.PLACING)
                    player_two_len = len(self.PLACING)
                else:
                    player_two = self.graphics.set_color("G", self.SELECTING)
                    player_two_len = len(self.SELECTING)
            else:
                player_two = " "
                player_two_len = 1
        elif isinstance(self.players[1], PlayerEasyAI):
            player_two = self.EASY
            player_two_len = len(self.EASY)
        elif isinstance(self.players[1], PlayerMediumAI):
            player_two = self.MEDIUM
            player_two_len = len(self.MEDIUM)
        else:
            player_two = self.HARD
            player_two_len = len(self.HARD)
        dsp += " " * ((39 - player_one_len) // 2) + player_one + " " *\
               ((39 - player_one_len) // 2)
        dsp += "|" if player_one_len % 2 == 1 else " |"
        dsp += " " * ((39 - player_two_len) // 2) + player_two + " " *\
               ((39 - player_two_len) // 2)
        dsp += "|#\n" if player_two_len % 2 == 1 else " |#\n"
        print(dsp + "##################################################"
                    "#################################")

    def display_piece_pool(self):
        """
        Displays the piece pool and selected piece in the game status display
        """
        self.piece_pool = dict({i: Piece(self.play.game.pieces[i]) for i in
                                self.play.game.pieces}.items())
        dsp = "#----------------------------------------------------------" \
              "-----------------------#\n#|"

        for i in range(8):
            dsp += "  " + str(i + 1) + ": " + self.piece_pool[str(i)].\
                get_chars() + " |" if str(i) in self.piece_pool.keys() \
                else "  " + str(i + 1) + ":     " + "|"
        dsp += "#\n#|  9: " + self.piece_pool['8'].get_chars() +\
               " |" if '8' in self.piece_pool.keys() else "#\n#|  9:     |"

        for i in range(9, 16):
            dsp += " " + str(i + 1) + ": " + self.piece_pool[str(i)].\
                get_chars() + " |" if str(i) in self.piece_pool.keys() \
                else " " + str(i + 1) + ":     " + "|"
        dsp += "#\n#------------------------------------------------------" \
               "---------------------------"

        if self.has_selected_piece():
            dsp += "#\n#|                              Selected Piece: " + \
                   self.selected_piece + "                              |#"
            dsp += "\n#---------------------------------------------------" \
                   "------------------------------"
        print(dsp + "#\n##################################################"
                    "#################################")

    def has_selected_piece(self):
        if self.play.selected_piece and \
                len([r for r in self.play.game.board if
                     self.play.selected_piece in r]) == 0:
            self.selected_piece = Piece(self.play.selected_piece).get_chars()
        else:
            self.selected_piece = None
        return self.selected_piece
