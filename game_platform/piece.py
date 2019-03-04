class Piece:
    """
    Creates a piece ASCII object for displaying on the game platform CLI
    Author(s): Adam Ross
    Last-edit-date: 28/02/2019
    """

    CHAR_ONE = "A"  # the first char for each piece, either upper or lower case
    CHAR_TWO = "B"  # the second char for each piece, either upper or lower case
    CHAR_THREE = "C"  # the third char for each piece, either upper or lower case
    TRUE_COL = '\033[94m'  # the fourth characteristic for each piece when true
    FALSE_COL = '\033[93m'  # the fourth characteristic for each piece when false
    END_COL = '\033[0m'  # to reset back to normal text colour

    def __init__(self, pce):
        """
        Initializes the piece with binary values for each characteristic
        :param pce: a string of binary values for each characteristic of piece
        """
        self.id = int(pce, 2)
        self.chars = self.CHAR_ONE if int(pce[0]) else self.CHAR_ONE.lower()
        self.chars += self.CHAR_TWO if int(pce[1]) else self.CHAR_TWO.lower()
        self.chars += self.CHAR_THREE if int(pce[2]) else self.CHAR_THREE.lower()
        self.chars = self.TRUE_COL + self.chars + self.END_COL if int(pce[3])\
            else self.FALSE_COL + self.chars + self.END_COL

    def get_chars(self):
        """
        Gets the string of characteristics for the piece
        :return: string of three upper/lower case chars in either red or black
        """
        return self.chars
