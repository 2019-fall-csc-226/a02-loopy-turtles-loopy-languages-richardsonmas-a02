# Author: Mason Richardson
# Username: richardsonmas
#
#
# Assignment A02
# Purpose: Draws a symbol with turtles.

import turtle
from cmath import sin

wn = turtle.Screen()
wn.bgcolor('#9476D0')
lefty = turtle.Turtle()
righty = turtle.Turtle()
lefty.pensize(5)
righty.pensize(5)
lefty.hideturtle()
righty.hideturtle()


righty.left(90)
lefty.left(90)
lefty.penup()
righty.penup()
righty.forward(150)
lefty.forward(150)
lefty.left(90)
righty.right(90)
righty.pendown()
lefty.pendown()
lefty.forward(100)
righty.forward(100)
lefty2 = turtle.Turtle()
righty2 = turtle.Turtle()
lefty2.pensize(5)
righty2.pensize(5)
lefty2.hideturtle()
righty2.hideturtle()
lefty2.penup()
righty2.penup()
righty2.setpos(100, 150)
lefty2.setpos(-100, 150)
righty2.pendown()
lefty2.pendown()
lefty.left(120)
righty.right(120)
lefty2.right(45)
righty2.right(135)
lefty.forward(180)
righty.forward(180)
lefty2.forward(210)
righty2.forward(210)
# these make the curly cue things on the ends. the basic things you have to control is the rate each angle curls in, and how much
# shorter each new segment will be.
for n in range(30):
    anglel1 = 2*n
    movel1 = 40*(1/(1+n))
    lefty.left(anglel1)
    lefty.forward(movel1)
for n in range(30):
    angler1 = 2*n
    mover1 = 40*(1/(1+n))
    righty.right(angler1)
    righty.forward(mover1)
lefty2.penup()
righty2.penup()
lefty2.setpos(0, -65)
righty2.setpos(0, -65)
lefty2.pendown()
righty2.pendown()
righty2.right(90)
lefty2.left(90)
for n in range(30):
    angler2 = 2*n
    mover2 = 18*(1/(1+n))
    righty2.left(angler2)
    righty2.forward(mover2)
for n in range(30):
    anglel2 = 2*n
    movel2 = 18*(1/(1+n))
    lefty2.right(anglel2)
    lefty2.forward(movel2)








wn.exitonclick()