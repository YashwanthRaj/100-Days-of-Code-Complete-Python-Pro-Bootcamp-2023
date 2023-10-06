# We have to program the turtle such that it randomly moves with diff colour
import random
import turtle
from turtle import Turtle, Screen

angela = Turtle()
direction_angles = [0, 90, 180, 270]
color_list = ['Green','Blue','Black', 'Grey', 'Yellow', 'Red', 'Orange', 'Cyan', 'Pink']
turtle_width = [2,4,5,8]
angela.speed('fastest')

for i in range(100):
    angela.color(random.choice(color_list))
    angela.width(random.choice(turtle_width))
    angela.forward(25)
    angela.setheading(random.choice(direction_angles))


screen_stop = Screen()
screen_stop.exitonclick()


# # There is another way that we can use to generate random colors
# # We can use the rgb module to do that
# # But to do that we need to change the turtle module itself, we need to assign the colormode to 255
#
# turtle.colormode(255) # Now we can assign rgb colors
# tim = Turtle()
#
# def color_assign():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     choise = (r,g,b)
#     return choise
#
#
# tim.forward(70)
# tim.color(color_assign())
# tim.right(90)
# tim.forward(90)
#
#
# screen_stop = Screen()
# screen_stop.exitonclick()