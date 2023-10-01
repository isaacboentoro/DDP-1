#  Collaborators: Flori Andrea Ng NPM:2306171713
import turtle
from tkinter import messagebox


#  Parameter data collection using turtle.numinput
def float_input_validator(title, prompt, minval, maxval) -> int:
    while True:
        user_input = turtle.numinput(title=title, prompt=prompt, minval=minval, maxval=maxval)
        if user_input != int(user_input):
            messagebox.showwarning(title="Type Error", message="Input must be an integer")
        else:
            return int(user_input)


num_towers = float_input_validator(title="Input", prompt="The number of towers you want to build (min 1)", minval=1,
                                   maxval=None)
tower_distance = float_input_validator(title="Input", prompt="Enter the distance between towers(integer)", minval=2,
                                       maxval=5)
tower_difference = float_input_validator(title="Tower Layer Difference", prompt="Enter the number of layer differences "
                                                                                "between each tower(integer)",
                                         minval=1, maxval=35)
brick_width = float_input_validator(title="Brick Widht", prompt="Enter the width of a brick (integer)", minval=1,
                                    maxval=35)
brick_height = float_input_validator(title="Brick Height", prompt="Enter the height of a brick", minval=1, maxval=25)
tower_height = float_input_validator(title="The number of First Tower Layers", prompt="Enter the number of layers for "
                                                                                      "the first tower(integer)",
                                     minval=1, maxval=None)
tower_width = float_input_validator(title="Layer Width", prompt="Enter the width of a layer(integer", minval=1,
                                    maxval=5)

turtle.penup()
turtle.goto(-700, -455)
turtle.speed('fastest')
turtle.Screen().bgpic('supermario.gif')  # set background image
turtle.Screen().screensize(10000, 5000)
turtle.Screen().tracer(0)  # Code for instantaneous output
brickCount = 0

mushroom_colors = ['red', "green", "blue", "orange", "purple"]  # List to iterate through mushroom 'hat' colors
# Arbitrary variable initialization to ensure variable is never undefined
layer = 0
tower_index = 0
turtle.hideturtle()
for towers in range(num_towers):
    initial_pos = turtle.pos()
    tower_index = 1
    tower_index += towers  # For every tower built, increase towerIndex by 1 to keep track of how many towers have
    # been built ,
    # Also functions to decide height for next towers
    for height in range(tower_height + (tower_index - 1) * tower_difference):
        for width in range(tower_width):
            brickCount += 1
            turtle.begin_fill()
            for lines in range(2):
                turtle.fillcolor("#CA7F65")
                turtle.pendown()
                turtle.forward(brick_width)
                turtle.right(90)
                turtle.forward(brick_height)
                turtle.right(90)
            turtle.end_fill()
            turtle.forward(brick_width)
        layer = 1
        layer += height  # Keep track of which layer turtle is on to know to move further up
        turtle.penup()
        turtle.setposition(initial_pos)
        turtle.goto(initial_pos + (0, layer * brick_height))
        turtle.pendown()
    turtle.penup()
    turtle.goto(initial_pos + (-brick_width / 2, layer * brick_height))
    # For every tower, create a 'head' using same method as brick rows
    turtle.fillcolor("#693424")
    for width in range(tower_width + 1):
        brickCount += 1
        turtle.begin_fill()
        for lines in range(2):
            turtle.pendown()
            turtle.forward(brick_width)
            turtle.right(90)
            turtle.forward(brick_height)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(brick_width)
    turtle.penup()
    turtle.goto(initial_pos + (tower_width * (3.5 / 8) * brick_width, (1 + layer) * brick_height))
    turtle.pendown()
    # Create mushroom
    color_index = (tower_index + int(turtle.xcor() // 100)) % len(mushroom_colors)
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(brick_width / 2)  # makes a square
        turtle.right(90)
    turtle.end_fill()
    turtle.fillcolor(mushroom_colors[color_index])
    turtle.begin_fill()
    turtle.forward(brick_width)
    turtle.left(90)
    turtle.circle(brick_width * 0.75, 180)
    turtle.left(90)  # makes a semicircle then connects it with the square
    turtle.forward(brick_width)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(initial_pos + (tower_distance * brick_width * tower_width, 0))
    # go to the right by distance * brick * width distance to the right to begin the next tower
turtle.goto(-700, -200)
turtle.write(f"{tower_index} Towers created with a total of {brickCount} bricks", font=("Arial", 25, "normal"))
# Code for instantaneous output
turtle.Screen().update()
turtle.Screen().mainloop()
turtle.hideturtle()
turtle.done()
