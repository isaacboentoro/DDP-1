from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''a simple pen drawing application'''
    def __init__(self, master):
        master.title("Scribble App")
        # mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0, 0
        self.color = '#8000FF'
        # create canvas 800 X 500
        self.canvas = Canvas(master, width=800, height=500)
        # bind mouse events to handlers:
        # -- pressing the left mouse button
        self.canvas.bind("<Button-1>", self.begin)
        # -- moving the mouse while holding/pressing left mouse button
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)
        # create a new frame for holding the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)
        self.bt_clear = Button(master=frame1, text="Clear", command=self.clear)
        self.bt_clear.pack(side=LEFT, padx=5)
        self.bt_color = Button(frame1, text="Color", command=self.choose_color)
        self.bt_color.pack(side=LEFT)
        self.message = Label(master, text="Draw something!")
        self.message.pack(side=BOTTOM)
        # start the event loop
        master.mainloop()

    def begin(self, event):
        '''handles left button click by recording mouse position as the start of the curve'''
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        '''handles mouse motion, while pressing left button, by connecting the previous mouse position to the new one'''
        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=5)
        self.oldx, self.oldy = event.x, event.y

    def clear(self):
        '''clears the canvas'''
        self.canvas.delete("all")

    def choose_color(self):
        '''opens a color chooser and sets the new color'''
        self.color = askcolor(color=self.color)[1]

if __name__ == "__main__":
    root = Tk()
    Scribble(root)