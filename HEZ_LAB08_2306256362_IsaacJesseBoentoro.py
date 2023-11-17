from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT, simpledialog
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''a simple pen drawing application'''
    def __init__(self, master):
        master.title("Scribble App")
        self.oldx, self.oldy = 0, 0
        self.color = '#8000FF'
        self.brush_size = 5  # Default brush size
        self.canvas = Canvas(master, width=800, height=500)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)
        frame1 = Frame(master)
        frame1.pack(side=TOP)
        self.bt_clear = Button(master=frame1, text="Clear", command=self.clear)
        self.bt_clear.pack(side=LEFT, padx=5)
        self.bt_color = Button(frame1, text="Color", command=self.choose_color, bg = self.color)
        self.bt_color.pack(side=LEFT)
        self.bt_brush_size = Button(frame1, text="Brush Size", command=self.choose_brush_size)
        self.bt_brush_size.pack(side=LEFT)
        self.message = Label(master, text="Draw something!")
        self.message.pack(side=BOTTOM)
        master.mainloop()

    def begin(self, event):
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill=self.color, width=self.brush_size, smooth = True, splinesteps = 20)
        self.oldx, self.oldy = event.x, event.y

    def clear(self):
        self.canvas.delete("all")

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]
        self.bt_color.config(bg=self.color)

    def choose_brush_size(self):
        self.brush_size = simpledialog.askinteger("Brush size", "Enter brush size:", minvalue=1, maxvalue=50)

if __name__ == "__main__":
    root = Tk()
    Scribble(root)