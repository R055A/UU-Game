from tkinter import Frame, Tk, Canvas

HEIGHT = 800  # test size
WIDTH = 800  # test size
BACKGROUND_COLOUR = 'white'


class GamePlatform(Frame):
    """
    The game platform GUI
    Author(s): Adam Ross
    Lase-edit-date: 21/02/2019
    """

    def __init__(self, master):
        """
        Initializes the GUI
        """
        super().__init__(master)
        self.master = master
        self.master.title("UU-Game")
        self.canvas = Canvas(
            height=HEIGHT, width=WIDTH,
            bg=BACKGROUND_COLOUR)
        self.canvas.pack()


# The following is temporary for running the GUI until CP integrated
gp = GamePlatform(master=Tk())
gp.mainloop()
