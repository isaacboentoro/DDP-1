## Author: Isaac Jesse Boentoro
## File name: lab02b.py
## using turtle to draw regular polygons
## prompt user for the number of sides and the color components (r,g,b)
import turtle
turtle.shape('turtle')
turtle.title('Lab 02')
# get the number of sides from user
sides = int(turtle.textinput("Lab 02", "The number of sides: "))
# draw the n-side polygon using a for loop
# the length of a side is getting shorter as n getting larger
# When n = 4, the length of a side is 100.

# get the value of red color from user
r = float(turtle.textinput("Lab 02","The red color component [between 0 and 1]: "))
# get the value of green color from user
g = float(turtle.textinput("Lab 02","The green color component [between 0 and 1]: "))# get the value of blue color from user
b = float(turtle.textinput("Lab 02","The blue color component [between 0 and 1]: "))
# create the color from rgb values given by user

# move the turtle to a new location

# draw a regular polygon with n sides and color(r,g,b)
# use a for loop
#use functions to avoid redundancy

def polygon(sides):
    for i in range(sides):
        turtle.forward(400/sides)
        turtle.right(360/sides)
#configuration
#turtle.speed(50) 
turtle.penup()
turtle.goto(-100,0) #initial polygon position
turtle.pendown()
polygon(sides)

turtle.penup()
turtle.goto(160,0)
turtle.pendown()
turtle.begin_fill()
turtle.color(r, g, b)
polygon(sides)
turtle.end_fill()
turtle.penup()
#make the turtle invisible
turtle.hideturtle()
# message for user
turtle.up()
turtle.goto(0,200)
turtle.down()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit ...",
False, align='center', font=('Arial', 20, 'normal'))
# wait for user to click on the screen to exit
turtle.exitonclick()
# the end