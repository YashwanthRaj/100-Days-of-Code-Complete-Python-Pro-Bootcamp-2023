# We have to draw a dashed line

from turtle import Turtle, Screen

tim = Turtle()

for i in range(10):
    tim.forward(10)
    tim.color('white')
    tim.forward(10)
    tim.color('black')

tim.left(90)

# Another Alternate program for this function
for j in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

space =Screen()
space.exitonclick()