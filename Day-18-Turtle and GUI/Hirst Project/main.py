# We are drawing Hirst spot painting with teh help of turtle module
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

## Colorgram is a package that lets you extract color from images, Below is the code to extract rbb values from image
#
# import colorgram as cg
#
# color_list = cg.extract("image.jpg", 60)
# color_palette = []
#
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     color_palette.append(new_color)
#
# print(color_palette)

painting = Turtle()

color_palette = [(253, 252, 246), (243, 254, 249), (253, 245, 251), (243, 245, 253), (213, 151, 106), (248, 247, 74), (87, 244, 200), (41, 12, 179), (224, 115, 161), (160, 10, 76), (17, 181, 76), (31, 6, 90), (223, 49, 138), (151, 88, 43), (118, 98, 228), (84, 34, 13), (9, 97, 45), (85, 6, 38), (183, 182, 241), (71, 216, 90), (178, 45, 104), (47, 16, 249), (34, 142, 47), (155, 134, 215), (173, 9, 7), (75, 244, 249), (228, 166, 205), (234, 47, 43), (87, 74, 148), (6, 96, 100), (16, 177, 184), (181, 12, 164), (11, 73, 24), (219, 132, 30), (234, 169, 166), (101, 60, 19), (251, 11, 9), (252, 253, 0), (3, 249, 246)]

def draw():
    painting.forward(1)
    painting.penup()
    painting.forward(50)
    painting.pendown()

def return_to_start_line():
    painting.penup()
    painting.left(90)
    painting.forward(50)
    painting.left(90)
    painting.forward(510)
    painting.left(180)
    painting.pendown()

painting.speed("fastest")

for i in range(0,10):
    for j in range(0,10):
        painting.color(random.choice(color_palette))
        painting.width(20)
        draw()
    return_to_start_line()


screen = Screen()
screen.exitonclick()



# # Angelas Solution
# import turtle as turtle_module
# import random
#
# turtle.colormode(255)
# tim = turtle.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
# screen = turtle.Screen()
# screen.exitonclick()