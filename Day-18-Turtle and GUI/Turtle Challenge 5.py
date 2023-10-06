# Make a Spirograph with each circle with a randomly generate color
import random
import turtle
from turtle import Turtle, Screen


turtle.colormode(255)
joy = Turtle()
joy.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ch = (r,g,b)
    return ch


def draw_circle(angle):
    joy.color(random_color())
    joy.circle(100)
    joy.right(angle)


for i in range(100):
    draw_circle(5)


screen = Screen()
screen.exitonclick()


## Alternate Solution
#
# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
# tim.speed('fastest')
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)