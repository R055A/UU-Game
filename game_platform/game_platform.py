from tkinter import *
from game_platform.piece import Piece

TITLE = 'UU-Game'
HEIGHT = 600  # test size
WIDTH = 600  # test size
BACKGROUND_COLOUR = 'white'
CELL_SIZE = 100
COLOUR_TRUE = 'grey1'
BORDER = 4
SIZE = 70


def key(event):
        print ("pressed",repr(event.char))


def test(event):
        self.canvas.focus_set()
        print("x = ",self.event.x, "y = ",self.event.y)
        
class GamePlatform(Frame):
    """
    The game platform GUI
    Author(s): Adam Ross, Gustav From, Pelle Ingvast
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
        root = Tk()
        self.canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOUR)
        #self.canvas = Canvas(height=HEIGHT, width=WIDTH, bg=BACKGROUND_COLOUR)
        self.canvas.bind("<Key>",key)
        self.canvas.bind("<ButtonRelease-1>", self.test)
        
        
        self.canvas.pack()
        self.pieces = dict({i: Piece(self.canvas, self.play.game.pieces[i])
                            for i in self.play.game.pieces}.items())
    
        #print(self.pieces['15'].shape)

        
        
        #self.canvas.pack()
        
        
        #print("x = ",self.event.x, "y = ",self.event.y)
        
        #self.canvas.delete(self.pieces['15'].shape)
        self.move('13')

        for n in range(2, 7):
            # vertical
            self.canvas.create_line(
                CELL_SIZE*n, 2*CELL_SIZE-BORDER/2,
                CELL_SIZE*n, HEIGHT+BORDER/2,
                width=BORDER, fill=COLOUR_TRUE)
            # horizontal
            self.canvas.create_line(
                2*CELL_SIZE-BORDER/2, CELL_SIZE*n,
                HEIGHT+BORDER/2, CELL_SIZE*n,
                width=BORDER, fill=COLOUR_TRUE)
        
        """
        self.canvas.bind("<ButtonRelease-1>", test)
        self.canvas.pack()
        root.mainloop()
        """
        root.mainloop()
    def move(self, piece):
        
        ##Pos on 4x4-board: (0 to 3)
        x_pos = 2
        y_pos = 1
        
        startX = CELL_SIZE*2 + x_pos*CELL_SIZE + (CELL_SIZE-SIZE)/2 #435
        stoppX = CELL_SIZE*3 + x_pos*CELL_SIZE - (CELL_SIZE-SIZE)/2 #465
        startY = CELL_SIZE*2 + y_pos*CELL_SIZE + (CELL_SIZE-SIZE)/2 #535
        stoppY = CELL_SIZE*3 + y_pos*CELL_SIZE - (CELL_SIZE-SIZE)/2 #565
        
        startX30 = startX + (CELL_SIZE-SIZE)
        stoppX30 = stoppX - (CELL_SIZE-SIZE)
        startY30 = startY + (CELL_SIZE-SIZE)
        stoppY30 = stoppY - (CELL_SIZE-SIZE)
        
        
        shapeStr = startX, startY, stoppX, stoppY
        verticalStr = startX30, startY, stoppX30, stoppY
        horizontalStr = startX, startY30, stoppX, stoppY30
        print(shapeStr)
        
        if(self.pieces[piece].shape):
            self.canvas.coords(self.pieces[piece].shape, shapeStr)
        if(self.pieces[piece].vertical):
            self.canvas.coords(self.pieces[piece].vertical, verticalStr)
        if(self.pieces[piece].horizontal):
            self.canvas.coords(self.pieces[piece].horizontal, horizontalStr)
        #self.canvas.coords(self.pieces[piece].shape, '200 300 270 370')
        #self.canvas.coords(self.pieces[piece].vertical, '230 300 240 370')
        #self.canvas.coords(self.pieces[piece].horizontal, '200 330 270 340')
        
        #print(self.canvas.)
        
        ##[115.0, 515.0, 185.0, 585.0], Shape
        ##[145.0, 515.0, 155.0, 585.0], Vertical
        ##[115.0, 545.0, 185.0, 555.0], Horizontal
        #print(self.canvas.coords(self.pieces[piece].horizontal))
        
        #self.pieces['15'] = Piece(self.pieces[piece], '400', '400')
        
        """
        if(self.pieces[piece].shape):
            self.canvas.delete(self.pieces[piece].shape)
            
        if(self.pieces[piece].vertical):
            self.canvas.delete(self.pieces[piece].vertical)
            
        if(self.pieces[piece].horizontal):
            self.canvas.delete(self.pieces[piece].horizontal)
         """ 
        
    def test(event):
        self.canvas.focus_set()
        print("x = ",self.event.x, "y = ",self.event.y)
        
        
    def key(event):
        print ("pressed",repr(event.char))