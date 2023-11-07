from turtle import *
import random

tracer(0, 0)


def sierpinski(length, depth):
    if depth == 1:
        colormode(255)  # Implement random coloring for triangles
        r = int(random.random() * 255)
        g = int(random.random() * 255)
        b = int(random.random() * 255)
        color(r, g, b)
    if depth > 1: dot()  # mark position to better see recursion
    if depth == 0:  # base case
        stamp()  # stamp a triangular shape
    else:
        forward(length)  # Create 3 sierpinski triangles within each sierpinski triangle
        sierpinski(length / 2, depth - 1)  # recursive call with reduced length and depth
        backward(length)  # Move to correct position
        left(120)
        forward(length)
        sierpinski(length / 2, depth - 1)
        backward(length)
        left(120)
        forward(length)
        sierpinski(length / 2, depth - 1)
        backward(length)
        left(120)


# create a drawing screen
ts = Screen()
ts.title("Colorful Sierpinski Fractal")
speed(0)  # Set drawing speed
left(90)
sierpinski(200, 6)  # Call sierpinski triangle function with parameters length 200 and depth 6
hideturtle()
update()
ts.exitonclick()
