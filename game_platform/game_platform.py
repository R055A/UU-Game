from tkinter import Tk, Canvas

HEIGHT = 800  # test size
WIDTH = 800  # test size
BACKGROUND_COLOUR = 'white'


class GamePlatform(Tk):
    """
    The game platform GUI
    Author(s): Adam Ross
    Lase-edit-date: 21/02/2019
    """

    def __init__(self):
        """
        Initializes the GUI
        """
        Tk.__init__(self)
        self.canvas = Canvas(
            height=HEIGHT, width=WIDTH,
            bg=BACKGROUND_COLOUR)
        self.canvas.pack()


# The following is temporary for running the GUI until CP integrated
gp = GamePlatform()
gp.mainloop()
