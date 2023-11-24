from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox

class DrawRubberShapes(object):
    # Construct the GUI
    def __init__(self):
        window = Tk() # Create a window
        window.title("Lab 09: Drawing Rubber Shapes")  # Set a title
        frame1 = Frame(window, width = 900, height = 600)  # Create and add a frame to window
        frame1.grid()
        # Create a button for choosing color using a color chooser
        self.fillColor = StringVar()
        self.fillColor.set('red')

        def colorCommand():
            (rgb, color) = askcolor()
            if color is not None:
                self.fillColor.set(color)
                colorButton["bg"] = color

        colorButton = Button(frame1, text="Color", command=colorCommand, bg=self.fillColor.get())

        colorButton.grid(row=1, column=1, columnspan=2)
        # Create radio buttons for geometrical shapes
        self.v1 = StringVar()
        rbRectangle = Radiobutton(frame1, text="Rectangle", variable=self.v1, value='R', command=self.drawRectangle)
        rbRectangle.grid(row=1, column=3)
        # Initialize the radio buttons for drawing shapes and assign unique values 
        rbOval = Radiobutton(frame1, text="Oval", variable=self.v1, value='O', command=self.drawOval)
        rbOval.grid(row=1, column=4)
        rbLine = Radiobutton(frame1, text="Line", variable = self.v1, value = 'L',command=self.drawLine)
        rbLine.grid(row=1, column=5)
        clearButton = Button(frame1, text="Clear", command=self.clearCanvas)
        clearButton.grid(row=1, column=6)
        self.v1.set('R') 
        # Set default shape to rectangle
        # Create a canvas, bound to mouse events
        self.canvas = Canvas(window, width=900, height=600, border = 5, relief = "groove")
        self.canvas.grid(row=2, column=0, columnspan=6)  # Changed from pack to grid
        self.canvas.bind('<ButtonPress-1>', self.onStart)  # left-click
        self.canvas.bind('<B1-Motion>', self.onGrow)  # and drag for drawing
        self.canvas.bind('<ButtonPress-3>', self.startMove)  # right-click
        self.canvas.bind('<B3-Motion>', self.moving)
        window.bind("<ButtonPress-3>", self.selectShape)
        window.bind("<KeyPress-d>", self.deleteShape)
        window.bind("<KeyPress-h>", self.showHelp)  # press 'h' for help info
        self.canvas.create_text(50, 15,text = "Press h for help")
        # for remembering the current object and shape
        self.object = None
        self.shape = self.canvas.create_rectangle # Set default shape
        window.mainloop() 


    def selectShape(self, event):
        self.object = self.canvas.find_closest(event.x, event.y)

    def deleteShape(self, event):
        if self.object:
            self.canvas.delete(self.object)
            self.object = None
        # Check if shape exits before deleting it

    def showHelp(self, event):
        messagebox.showinfo("Click & Move", "Mouse Commands:\n\tLeft+Drag = Draw new rubber shape\nRight = Selecct a shape\nRight+Drag = Move selected shape\n'd' = Delete selected shape\n'h' = Show this help message")
    
    def clearCanvas(self):
        self.canvas.delete("all") 
        # Delete all objects on canvas

    def drawRectangle(self):
        self.shape = self.canvas.create_rectangle

    def drawOval(self):
        self.shape = self.canvas.create_oval

    def drawLine(self):
        self.shape = self.canvas.create_line
        
    # Define functions for drawing shapes

    def onStart(self, event):
        self.start = event
        self.object = self.shape(self.start.x, self.start.y, self.start.x, self.start.y, fill=self.fillColor.get())
        # Create object based on dragging mouse
    def startMove(self, event):
        self.startMoving = event
        objectTuple = self.canvas.find_closest(event.x, event.y)
        if objectTuple != ():
            self.object = objectTuple[0]

    def moving(self, event):
        canvas = event.widget
        if self.object:
            canvas.move(self.object, event.x - self.startMoving.x,event.y - self.startMoving.y)
            self.startMoving = event 
            # Move object by x and y coordinates based on how far the user moved its mouse
    # elastic drawing: delete and redraw, repeatedly
    def onGrow(self, event):
        canvas = event.widget
        if self.object: canvas.delete(self.object)
        if self.shape == self.canvas.create_line:
            objectId = self.shape(self.start.x, self.start.y, event.x,
            event.y, fill=self.fillColor.get())
        else: # Add an exception if the current shape tool is line and not call outline parameter
            objectId = self.shape(self.start.x, self.start.y, event.x,
                event.y, fill=self.fillColor.get(),
                outline=self.fillColor.get())
        self.object = objectId

if __name__ == '__main__':
    DrawRubberShapes()