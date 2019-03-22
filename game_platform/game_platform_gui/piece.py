#!/usr/bin/env python3

class Piece:
    """
    Creates a piece object for displaying on the game platform GUI
    Author(s): Adam Ross
    Last-edit-date: 22/02/2019
    """

    COL_TRUE = 'red'  # the colour of the true first characteristic
    COL_FALSE = 'gray1'  # the colour of the false first characteristic
    HORIZONTAL = 'snow'  # the colour of the horizontal line
    VERTICAL = 'snow'  # the colour of the vertical line
    SIZE = 65  # size of each shape height and width
    BORDER = 2  # size of each shape border outline
    SHAPE_MARGIN = 17.5  # the margin surrounding object from x, y coords
    LINE_MARGIN = 35  # the margin from the x or y coord that the line starts
    CELL_SIZE = 100  # the width and height dimension for each game board cell

    def __init__(self, canvas, pce, x=None, y=None):
        """
        Initializes the piece with binary values for each characteristic
        :param canvas: widget for drawing objects
        :param pce: a string of binary values for each characteristic of piece
        :param x: the x coordinate of the top left corner of the piece image
        :param y: the y coordinate of the top left corner of the piece image
        """
        self.pce = int(pce, 2)
        self.canvas = canvas
        self.x_pos, self.y_pos = (x, y) if x else self.set_coords()
        self.colour = self.COL_TRUE if int(pce[3]) else self.COL_FALSE
        self.shape = self.draw_circle() if int(pce[2]) else self.draw_square()
        self.horizontal = self.draw_horizontal() if int(pce[0]) else None
        self.vertical = self.draw_vertical() if int(pce[1]) else None
        self.id = self.set_id()

    def set_coords(self):
        """
        Sets the coordinates of the piece object at initialization
        :param pce: the piece converted to an integer value
        :return: the x and y coordinates for the placement of the piece object
        """
        if self.pce < 4:
            return self.pce * self.CELL_SIZE + self.SHAPE_MARGIN, self.pce +\
                   self.SHAPE_MARGIN
        elif self.pce < 8:
            return (self.pce - 4) * self.CELL_SIZE + self.SHAPE_MARGIN, \
                   self.CELL_SIZE + self.SHAPE_MARGIN
        elif self.pce < 12:
            return self.SHAPE_MARGIN, (self.pce - 6) * self.CELL_SIZE + \
                   self.SHAPE_MARGIN
        else:
            return self.CELL_SIZE + self.SHAPE_MARGIN, (self.pce - 10) * \
                   self.CELL_SIZE + self.SHAPE_MARGIN

    def draw_circle(self):
        """
        Draws a circle shaped piece
        :return: the drawn circle shape
        """
        return self.canvas.create_oval(self.x_pos, self.y_pos, self.x_pos +
                                       self.SIZE, self.y_pos + self.SIZE,
                                       outline=self.colour, fill=self.colour,
                                       width=self.BORDER)

    def draw_square(self):
        """
        Draws a square shaped piece
        :return: the drawn square shape
        """
        return self.canvas.create_rectangle(self.x_pos, self.y_pos, self.x_pos
                                            + self.SIZE, self.y_pos +
                                            self.SIZE, outline=self.colour,
                                            fill=self.colour,
                                            width=self.BORDER)

    def draw_horizontal(self):
        """
        Draws a horizontal line through a piece object
        :return: the drawn horizontal line shape
        """
        return self.canvas.create_rectangle(self.x_pos, self.y_pos +
                                            self.LINE_MARGIN, self.x_pos +
                                            self.SIZE,
                                            self.y_pos + self.SIZE -
                                            self.LINE_MARGIN,
                                            outline=self.HORIZONTAL,
                                            fill=self.HORIZONTAL,
                                            width=self.BORDER)

    def draw_vertical(self):
        """
        Draws a vertical line through a piece object
        :return: the drawn vertical line shape
        """
        return self.canvas.create_rectangle(self.x_pos + self.LINE_MARGIN,
                                            self.y_pos, self.x_pos + self.SIZE
                                            - self.LINE_MARGIN, self.y_pos +
                                            self.SIZE, outline=self.VERTICAL,
                                            fill=self.VERTICAL,
                                            width=self.BORDER)

    def set_id(self):
        """
        Adds an ID number to the top left of each piece in the piece pool
        :return: the piece id text
        """
        return self.canvas.create_text(self.x_pos - 10, self.y_pos,
                                       fill=self.COL_FALSE, font="Times 10",
                                       text=str(self.pce + 1)) \
            if (self.x_pos, self.y_pos) == self.set_coords() else None
