import turtle

def inputValidation(title, prompt, minValue=None, maxValue=None): #input validation function with flexible parameters
    while True: #Persistently ask for user input until correct
        userInput = turtle.textinput(title, prompt)
        if userInput is None: #If user pressed 'cancel'
            return None
        try:
            userInput = int(userInput) #Make sure input is not float or string, but int.
            #Check if value is within range
            if (minValue is None or userInput>= int(minValue)) and (maxValue is None or userInput <= int(maxValue)):
                return userInput
            else:
                print(f"Input must be between {minValue} and {maxValue}")
                #Print error message when value is not between set parameters

        except ValueError: #Error case for try statement
            print("Invalid input. Please enter a valid number")

#Get tower parameters
#Towers to build

title = "Tower to build"
prompt = "Enter the amount of towers you want to build (integer)"
numTowers = inputValidation(title, prompt, minValue=1, maxValue=None)

#Distance between towers

title = "Distance between towers"
prompt = "Enter the distance between towers (integer)"
towerDistance = inputValidation(title, prompt, minValue = 2, maxValue = 5)

#Tower Layer difference

title = "Tower Layer Difference"
prompt = "Enter the number of layer differences between each tower (integer)"
towerDifference = inputValidation(title, prompt, minValue = 2, maxValue = 5)

#Get brick parameters
#Brick Length

title = "Brick Length"
prompt = "Enter brick length (max 35)"
brickLength = inputValidation(title, prompt, minValue=1, maxValue=35 )

title = "Brick Width"
prompt = "Enter brick length (max 25)"
brickWidth = inputValidation(title, prompt, minValue=1, maxValue=25)

#Get input with parameters minValue = 1, maxValue = 35
#Title and prompt could be implemented in the same way but this is more readable

#Tower body width
title = "Tower Body Width"
prompt = "Enter tower body width (max 10 bricks)"
towerWidth = inputValidation(title, prompt, minValue = 1, maxValue = 10)

baseTowerheight = 3
towerHeight = 1
for i in range(numTowers):
    for x in range(towerHeight):
        for y in range(towerWidth):
            initialPos = turtle.pos()
            for z in range(2):
                turtle.pendown()
                turtle.forward(brickWidth)
                turtle.right(90)
                turtle.forward(brickLength)
                turtle.right(90)
            turtle.forward(brickWidth)
        turtle.penup()
        turtle.goto(initialPos)
        

            


turtle.exitonclick()



