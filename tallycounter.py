from tkinter import *


class Counter(object):
    def __init__(self):
        self._value = 0

    def increment(self):
        self._value = (self._value + 1) % 10000
        return self

    def decrement(self):
        self._value -= 1

    def view(self):
        return f"{self._value:04d}"

    def reset(self):
        self._value = 0

    def set(self, new_value):
        self._value = (new_value % 10000)


class GuiCounter:
    def __init__(self):
        self._value = 0
        window = Tk()
        self._label = Label(window, text = f"{self._value:04d}" )
        increment_button = Button(window, text = "Increment", fg = "blue", command = self.increment)
        decrement_button = Button(window, text = "Decrement", fg = "green", command = self.decrement)
        reset_button  = Button(window, text = "Reset", fg = "red", command = self.reset)
        self._label.pack()
        increment_button.pack()
        decrement_button.pack()
        reset_button.pack()
        window.mainloop()

    def increment(self):
        self._value = (self._value + 1 ) % 10000
        self._label.config(text = f"{self._value:04d}")

    def decrement(self):
        self._value = (self._value -1 ) % 10000
        self._label.config(text = f"{self._value:04d}")

    def reset(self):
        self._value = 0
        self._label.config(text = f"{self._value:04d}")

counter = GuiCounter()

