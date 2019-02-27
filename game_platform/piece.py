CHAR_ONE = "A"  # the first char for each piece, either upper or lower case
CHAR_TWO = "B"  # the second char for each piece, either upper or lower case
CHAR_THREE = "C"  # the third char for each piece, either upper or lower case
TRUE_COL = '\033[94m'  # the fourth characteristic for each piece when true
FALSE_COL = '\033[93m'  # the fourth characteristic for each piece when false
END_COL = '\033[0m'  # to reset back to normal text colour


class Piece:
    """
    Creates a piece ASCII object for displaying on the game platform CLI
    Author(s): Adam Ross
    Last-edit-date: 27/02/2019
    """

    def __init__(self, pce, x=None, y=None):
        """
        Initializes the piece with binary values for each characteristic
        :param pce: a string of binary values for each characteristic of piece
        :param x: the column coordinate of the piece on the board
        :param y: the row coordinate of the piece on the board
        """
        self.id, self.x_pos, self.y_pos = int(pce, 2), x, y
        self.chars = CHAR_ONE if int(pce[0]) else CHAR_ONE.lower()
        self.chars += CHAR_TWO if int(pce[1]) else CHAR_TWO.lower()
        self.chars += CHAR_THREE if int(pce[2]) else CHAR_THREE.lower()
        self.chars = TRUE_COL + self.chars + END_COL if int(pce[3]) else \
            FALSE_COL + self.chars + END_COL

    def get_chars(self):
        """
        Gets the string of characteristics for the piece
        :return: string of three upper/lower case chars in either red or black
        """
        return self.chars
