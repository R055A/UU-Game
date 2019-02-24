from tkinter import Frame, Canvas
from game_platform.piece import Piece
from game_platform.board import Board

TITLE = 'UU-Game'
HEIGHT = 800  # test size
WIDTH = 800  # test size
BACKGROUND_COLOUR = 'white'


class GamePlatform(Frame):
    """
    The game platform GUI
    Author(s): Adam Ross
    Last-edit-date: 21/02/2019
    """

    def __init__(self, master, play):
        """
        Initializes the GUI
        :param master: the parent widget
        :param play: Play class instance
        """
        super().__init__(master)
        self.master = master
        self.play = play
        self.master.title(TITLE)
        self.canvas = Canvas(height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOUR)
        self.canvas.pack()
        self.pieces = dict({i: Piece(self.canvas, self.play.game.pieces[i])
                            for i in self.play.game.pieces}.items())
        self.board = Board(self.canvas, 10, 300, 300)
