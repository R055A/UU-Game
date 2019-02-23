COLOUR_TRUE = 'red'  # the colour of the true first characteristic
COLOUR_FALSE = 'gray1'  # the colour of the false first characteristic
HORIZONTAL = 'snow'  # the colour of the horizontal line
VERTICAL = 'snow'  # the colour of the vertical line
SIZE = 70  # size of each shape height and width
BORDER = 2  # size of each shape border outline
SHAPE_MARGIN = 15  # the margin surrounding the object from x and/or y coords
LINE_MARGIN = 30  # the margin from the x or y coord that the line starts
CELL_SIZE = 100  # the width and height dimension for each game board cell


class Piece:
    """
    Creates a piece object for displaying on the game platform GUI
    Author(s): Adam Ross
    Last-edit-date: 22/02/2019
    """

    def __init__(self, canvas, pce, x=None, y=None):
        """
        Initializes the piece with binary values for each characteristic
        :param canvas: widget for drawing objects
        :param pce: a string of binary values for each characteristic of piece
        :param x: the x coordinate of the top left corner of the piece image
        :param y: the y coordinate of the top left corner of the piece image
        """
        self.canvas = canvas
        self.x_pos, self.y_pos = (x, y) if x else self.set_coords(int(pce, 2))
        self.colour = COLOUR_TRUE if int(pce[0]) else COLOUR_FALSE
        self.shape = self.draw_circle() if int(pce[1]) else self.draw_square()
        self.horizontal = self.draw_horizontal() if int(pce[2]) else None
        self.vertical = self.draw_vertical() if int(pce[3]) else None

    @staticmethod
    def set_coords(pce):
        """
        Sets the coordinates of the piece object at initialization
        :param pce: the piece converted to an integer value
        :return: the x and y coordinates for the placement of the piece object
        """
        if pce < 4:
            return pce * CELL_SIZE + SHAPE_MARGIN, pce + SHAPE_MARGIN
        elif pce < 8:
            return (pce - 4) * CELL_SIZE + SHAPE_MARGIN, CELL_SIZE +\
                   SHAPE_MARGIN
        elif pce < 12:
            return SHAPE_MARGIN, (pce - 6) * CELL_SIZE + SHAPE_MARGIN
        else:
            return CELL_SIZE + SHAPE_MARGIN, (pce - 10) * CELL_SIZE +\
                   SHAPE_MARGIN

    def draw_circle(self):
        """
        Draws a circle shaped piece
        :return: the drawn circle shape
        """
        return self.canvas.create_oval(self.x_pos, self.y_pos, self.x_pos +
                                       SIZE, self.y_pos + SIZE, outline=self.
                                       colour, fill=self.colour, width=BORDER)

    def draw_square(self):
        """
        Draws a square shaped piece
        :return: the drawn square shape
        """
        return self.canvas.create_rectangle(self.x_pos, self.y_pos, self.x_pos
                                            + SIZE, self.y_pos + SIZE,
                                            outline=self.colour, fill=self.
                                            colour, width=BORDER)

    def draw_horizontal(self):
        """
        Draws a horizontal line through a piece object
        :return: the drawn horizontal line shape
        """
        return self.canvas.create_rectangle(self.x_pos, self.y_pos +
                                            LINE_MARGIN, self.x_pos + SIZE,
                                            self.y_pos + SIZE - LINE_MARGIN,
                                            outline=HORIZONTAL,
                                            fill=HORIZONTAL, width=BORDER)

    def draw_vertical(self):
        """
        Draws a vertical line through a piece object
        :return: the drawn vertical line shape
        """
        return self.canvas.create_rectangle(self.x_pos + LINE_MARGIN, self.
                                            y_pos, self.x_pos + SIZE -
                                            LINE_MARGIN, self.y_pos + SIZE,
                                            outline=VERTICAL, fill=VERTICAL,
                                            width=BORDER)
