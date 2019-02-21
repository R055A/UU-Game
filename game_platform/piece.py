COLOUR_TRUE = 'red'  # the colour of the true first characteristic
COLOUR_FALSE = 'gray1'  # the colour of the false first characteristic
HORIZONTAL = 'snow'  # the colour of the horizontal line
VERTICAL = 'snow'  # the colour of the vertical line
SIZE = 70  # size of each shape height and width
BORDER = 2  # size of each shape border outline


class Piece:
    """
    Creates a piece object for displaying on the game platform GUI
    Author(s): Adam Ross
    Last-edit-date: 21/02/2019
    """

    def __init__(self, canvas, pce):
        """
        Initializes the piece with binary values for each characteristic
        :param canvas:
        :param pce: a string of binary values for each characteristic of piece
        """
        self.canvas = canvas
        self.x_pos, self.y_pos = self.get_coords(int(pce, 2))
        self.colour = COLOUR_TRUE if int(pce[0]) else COLOUR_FALSE

        if int(pce[1]):  # if first characteristic is circle or square
            self.draw_circle()
        else:
            self.draw_square()

        if int(pce[2]):  # if second characteristic is horizontal line or not
            self.draw_horizontal()

        if int(pce[3]):  # if third characteristic is vertical line or not
            self.draw_vertical()

    @staticmethod
    def get_coords(pce):
        """

        :param pce: the piece converted to an integer value
        :return: the x and y coordinates for the placement of the piece object
        """
        return pce + 15, pce + 15  # temporary prior to the add 16 pieces task

    def draw_circle(self):
        """
        Draws a circle shaped piece
        """
        self.canvas.create_oval(self.x_pos, self.y_pos, self.x_pos + SIZE,
                                self.y_pos + SIZE, outline=self.colour,
                                fill=self.colour, width=BORDER)

    def draw_square(self):
        """
        Draws a square shaped piece
        """
        self.canvas.create_rectangle(self.x_pos, self.y_pos, self.x_pos + SIZE,
                                     self.y_pos + SIZE, outline=self.colour,
                                     fill=self.colour, width=BORDER)

    def draw_horizontal(self):
        """
        Draws a horizontal line through a piece object
        """
        self.canvas.create_rectangle(self.x_pos, self.y_pos + 30, self.x_pos +
                                     SIZE, self.y_pos + SIZE - 30,
                                     outline=HORIZONTAL, fill=HORIZONTAL,
                                     width=BORDER)

    def draw_vertical(self):
        """
        Draws a vertical line through a piece object
        """
        self.canvas.create_rectangle(self.x_pos + 30, self.y_pos, self.x_pos +
                                     SIZE - 30, self.y_pos + SIZE,
                                     outline=VERTICAL, fill=VERTICAL,
                                     width=BORDER)
