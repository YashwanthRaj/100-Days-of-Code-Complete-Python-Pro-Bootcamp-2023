# We have to draw triangle, square, pentagon, hexagon, septagon, octagon, nonagon and decagon
# Hint - Angles are 360 / (no. of sides)

import random
from turtle import Turtle, Screen

# tim = Turtle()
#
# # For Triange
# for i in range(3):
#     tim.color('Blue')
#     tim.forward(100)
#     tim.right(120)
#
# # For Square
# for j in range(4):
#     tim.color('Green')
#     tim.forward(100)
#     tim.right(90)
#
# # For Pentagon
# for j in range(5):
#     tim.color('Yellow')
#     tim.forward(100)
#     tim.right(72)
#
#
# # For Hexagon
# for j in range(6):
#     tim.color('Orange')
#     tim.forward(100)
#     tim.right(60)
#
#
# # For Septagon
# for j in range(7):
#     tim.color('Red')
#     tim.forward(100)
#     tim.right(51.4)
#
#
# # For Octagon
# for j in range(8):
#     tim.color('Pink')
#     tim.forward(100)
#     tim.right(45)
#
#
# # For Nonagon
# for j in range(9):
#     tim.color('Blue')
#     tim.forward(100)
#     tim.right(40)
#
#
# # For Decagon
# for j in range(10):
#     tim.color('Black')
#     tim.forward(100)
#     tim.right(36)


# Alternatively, we can simplify the code by doing this

timmy = Turtle()


def draw_figure(no_of_sides, color1):
    angle = 360 / no_of_sides
    timmy.color(color1)
    for i in range(no_of_sides):
        timmy.forward(100)
        timmy.right(angle)


j = 3
while j <11:
    color_list = ['Green','Blue','Black', 'Grey', 'Yellow', 'Red', 'Orange', 'Cyan', 'Pink']
    draw_figure(j,random.choice(color_list))
    j += 1


screen_stop = Screen()
screen_stop.exitonclick()