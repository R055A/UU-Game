COLOUR_TRUE = 'red'
COLOUR_FALSE = 'gray1'
SHAPE_TRUE = None
SHAPE_FALSE = None
SOLID_TRUE = None
SOLID_FALSE = None
LINE_TRUE = None
LINE_FALSE = None


class Piece:
    """
    Creates a piece image for displaying on the game platform GUI
    Author(s): Adam Ross
    Last-edit-date: 20/02/2019
    """

    def __init__(self, pce):
        """
        Initializes the piece with binary values for each characteristic
        :param pce: a string of binary values for each characteristic of piece
        """
        self.x_pos = int(pce, 2)  # example - converts binary to int
        self.y_pos = 0 if int(pce, 2) < 8 else 1  # example
        self.char_one = pce[0]  # the first characteristic binary value of the piece
        self.char_two = pce[1]  # the second characteristic binary value of the piece
        self.char_three = pce[2]  # the third characteristic binary value of the piece
        self.char_four = pce[3]  # the fourth characteristic binary value of the piece
        self.create_pce()  # creates the piece image for displaying

    def create_pce(self):
        """
        Sets the displayed attributes for the piece
        """

        if self.char_one:
            self.char_one = COLOUR_TRUE
        else:
            self.char_one = COLOUR_FALSE

        if self.char_two:
            self.char_two = SHAPE_TRUE
        else:
            self.char_two = SHAPE_FALSE

        if self.char_three:
            self.char_three = SOLID_TRUE
        else:
            self.char_three = SOLID_FALSE

        if self.char_four:
            self.char_four = LINE_TRUE
        else:
            self.char_four = LINE_FALSE
