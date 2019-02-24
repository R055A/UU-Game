import tkinter as tk


class Board(tk.Frame):

    def __init__(self, x=5):

        super().__init__()

        self.initUI(x)

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
