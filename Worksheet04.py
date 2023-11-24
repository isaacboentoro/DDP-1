from tkinter import *

class GrowShrinkCanvas(object):
    def __init__(self):
        window = Tk()
        window.title("Grow Shrink")
        self._canvas = Canvas(window, bg = "yellow", width = 200, height = 200)
        self._canvas.pack()
        self._canvas.bind("<Button-1>", self.shrink)
        self._canvas.bind("<Button-3>", self.grow)
        window.mainloop()

    def grow(self, event):
        self._canvas["width"] = int(self._canvas["width"]) + 10
        self._canvas["height"] = int(self._canvas["height"]) + 10

    def shrink(self, event):
        self._canvas["width"] = int(self._canvas["width"]) - 10
        self._canvas["height"] = int(self._canvas["height"]) - 10

GrowShrinkCanvas()