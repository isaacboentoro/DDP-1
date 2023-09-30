## turtleSample01.py
## using turtle to draw a triangle
import turtle
# let's start up a Turtle Graphics window with a geen turtle
turtle.color('green')
# put its pen down so all movement will show as a green line
#calculate appropriate angle
angle = 360/6
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)
turtle.forward(100)
turtle.right(angle)

#make green hexagon 

turtle.hideturtle()
# wait for user to click on the screen to exit
turtle.exitonclick()