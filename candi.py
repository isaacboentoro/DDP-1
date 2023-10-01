import turtle

layers = 5
brickWidth = 30
brickHeight = 15
layerWidth = 7
turtle.speed(5)
for layer in range(layers):
    initialPos = turtle.pos()
    layerIndex = 1
    layerIndex += layer
    
    for width in range(layerWidth - (2*layer) ):
        turtle.begin_fill()
        for lines in range(2):
            turtle.fillcolor('pink')
            turtle.pendown()
            turtle.forward(brickWidth)
            turtle.right(90)
            turtle.forward(brickHeight)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(brickWidth)
    turtle.penup()
    turtle.setposition(initialPos)
    turtle.goto(initialPos+(brickWidth, brickHeight))
    turtle.pendown()

turtle.exitonclick()