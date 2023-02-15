#Jason Galvao
#CS 175L-01
#turtle graphics stop sign

import math
import turtle

windWidth = 600
windHeight = 600
animSpeed = 0
numSides = 8
length = 100
angle = 45
textX = -5
textY = -10
turtleNum = 0

turtle.setup(windWidth, windHeight)

s = length
x = s / math.sqrt(2)
diameter = s + (2 * x)


turtle.color('red')
style = ('arial', 30, 'bold')
while turtleNum <= 7:
    turtle.forward(100)
    turtle.right(45)
    turtleNum = turtleNum + 1

turtle.right(85)
turtle.up()
turtle.forward(x * 2)
turtle.write("STOP",font=style)
