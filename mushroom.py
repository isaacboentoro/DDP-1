import turtle
brickWidth = 30
brickHeight = 15
def draw_eye(x, y, scale):
    turtle.penup()
    turtle.goto(x, y - 4 * scale)  # Position for the pupil
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(2 * scale)  # Pupil
    turtle.end_fill()

def draw_mushroom(brickWidth, brickHeight):
    reference_width = 30  # Reference width for proportions

    # Calculate scaling factors for brickWidth and brickHeight
    width_scale = brickWidth / reference_width
    height_scale = brickHeight / (reference_width * 2)  # Assuming the height is twice the reference width

    cornerPos = turtle.pos()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(brickWidth / 2)  # makes a square
        turtle.right(90)
    turtle.end_fill()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.forward(brickWidth)
    turtle.left(90)
    turtle.circle(brickWidth * 0.75, 180)
    turtle.left(90)  # makes a semicircle then connects it with the square
    turtle.forward(brickWidth)
    turtle.end_fill()

    # Calculate eye positions based on scaling factors
    eye_x1 = cornerPos[0] + (brickWidth * 0.25 * width_scale)
    eye_y = cornerPos[1] + (brickHeight * height_scale)
    eye_x2 = cornerPos[0] + (brickWidth * 0.75 * width_scale)

    # Draw the pupils only (black circles)
    turtle.penup()
    draw_eye(eye_x1, eye_y, width_scale)

    turtle.penup()
    draw_eye(eye_x2, eye_y, width_scale)

draw_mushroom(brickWidth, brickHeight)
turtle.exitonclick()