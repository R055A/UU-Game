from game_platform.piece import Piece


class GamePlatform:
    """
    The GamePlatform class
    Author(s): Adam Ross
    Last-edit-date: 05/03/2019
    """

    def __init__(self, play):
        """
        GamePlatform class constructor
        :param play: instance of the Play() class
        """
        self.play = play
        self.piece_pool = None
        self.selected_piece = None

    def display_game_status(self):
        """
        Displays the current game status of the players, board and piece pool
        """
        self.display_piece_pool()

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
               " |" if '8' in self.piece_pool.keys() else "\n|  9:    "

        for i in range(9, 16):
            dsp += " " + str(i + 1) + ": " + self.piece_pool[str(i)].\
                get_chars() + " |" if str(i) in self.piece_pool.keys() \
                else "  " + str(i + 1) + ":    " + "|"
        dsp += "#\n#------------------------------------------------------" \
               "---------------------------"

        if self.play.selected_piece and \
                len([r for r in self.play.game.board if
                     self.play.selected_piece in r]) == 0:
            self.selected_piece = Piece(self.play.selected_piece).get_chars()
            dsp += "#\n#|                              Selected Piece: " + \
                   self.selected_piece + "                              |#"
            dsp += "\n#---------------------------------------------------" \
                   "------------------------------"
        print(dsp + "#\n##################################################"
                    "#################################")
