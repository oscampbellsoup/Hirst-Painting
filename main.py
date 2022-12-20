# Import turtle and random modules
from turtle import Turtle, Screen
import random
# # Used colorgram module to extract colors from image and turn them into tuples list of RGB colors
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dot_painting.png', 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
colors_list = [(239, 230, 221), (231, 153, 82), (119, 171, 203), (0, 0, 0), (39, 110, 159), (240, 200, 80), (160, 59, 83), (200, 83, 111), (215, 132, 159), (23, 137, 102), (223, 83, 61), (119, 189, 154), (158, 164, 48), (188, 212, 222), (244, 156, 174), (47, 171, 134), (230, 197, 214), (28, 164, 194), (197, 221, 212), (161, 74, 52), (9, 102, 78), (242, 164, 153), (115, 43, 56), (108, 115, 171), (151, 214, 194), (148, 208, 225), (178, 181, 215), (42, 60, 103), (110, 46, 44), (34, 66, 83), (30, 65, 63), (41, 73, 77), (74, 47, 61), (255, 255, 0), (0, 255, 255)]
# Define screen object
screen = Screen()
# Set colormode attribute to 255
screen.colormode(255)
# Define turtle object
turtle = Turtle()
# Set hideturtle attribute
turtle.hideturtle()
# Set turtle speed attribute to fastest
turtle.speed(0)


# Define start position function
def start_pos():
    turtle.penup()
    turtle.right(90)
    turtle.forward(325)
    turtle.right(90)
    turtle.forward(292.5)
    turtle.right(180)


# Define circle stamp in row function
def circle_stamp_in_row():
    for c in range(10):
        turtle.pendown()
        turtle.dot(20, random.choice(colors_list))
        turtle.penup()
        turtle.forward(50)


# Define new row function
def new_row():
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)


# Hirst painting creation
start_pos()
for i in range(10):
    circle_stamp_in_row()
    new_row()


# Set screen attribute to exit on click
screen.exitonclick()
