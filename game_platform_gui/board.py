#!/usr/bin/env python3

import tkinter as tk


class Board(tk.Frame):

    def __init__(self, canvas, s=10, x= 10, y= 10):
        """
        Initializes the board
        :param canvas: widget for drawing objects
        :param s: the size modifier
        :param x: the x coordinate of the top left corner of the board image
        :param y: the y coordinate of the top left corner of the board image
        """
        super().__init__()

        canvas.create_rectangle(5*s+x, 5*s+y, 45*s+x, 45*s+y)
        # create vertical lines
        canvas.create_line(5*s+x, 15*s+y, 45*s+x, 15*s+y)
        canvas.create_line(5*s+x, 25*s+y, 45*s+x, 25*s+y)
        canvas.create_line(5*s+x, 35*s+y, 45*s+x, 35*s+y)
        # create horizontal lines
        canvas.create_line(15*s+x, 5*s+y, 15*s+x, 45*s+y)
        canvas.create_line(25*s+x, 5*s+y, 25*s+x, 45*s+y)
        canvas.create_line(35*s+x, 5*s+y, 35*s+x, 45*s+y)

    def initUI(self, x):

        self.master.title("Lines")
        self.pack(fill=tk.BOTH, expand=1)
        canvas = tk.Canvas(self)
        # create borders of the board
        canvas.create_rectangle(10*x, 5*x, 90*x, 85*x)
        # create vertical lines
        canvas.create_line(10*x, 25*x, 90*x, 25*x)
        canvas.create_line(10*x, 45*x, 90*x, 45*x)
        canvas.create_line(10*x, 65*x, 90*x, 65*x)
        # create horizontal lines
        canvas.create_line(30*x, 5*x, 30*x, 85*x)
        canvas.create_line(50*x, 5*x, 50*x, 85*x)
        canvas.create_line(70*x, 5*x, 70*x, 85*x)

        canvas.pack(fill=tk.BOTH, expand=1)


def main():

    x = 5
    root = tk.Tk()
    ex = Board(x)
    root.geometry(str(x*100)+"x"+str(x*100)+"+250+100")
    root.mainloop()


if __name__ == '__main__':
    main()
