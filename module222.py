#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Shyed Shahriar Housaini
#
# Created:     07/12/2019
# Copyright:   (c) Shyed Shahriar Housaini 2019
# Licence:     <your licence, "Shyed Shahriar Housaini Terms and Conditions">
#-------------------------------------------------------------------------------
from turtle import Turtle, Screen

SIZE = 100

def draw_O(turtle):
    turtle.pendown()
    for _ in range(4):
        turtle.forward(SIZE)
        turtle.left(90)
    turtle.penup()

def draw_S(turtle):
    position = turtle.position()
    turtle.pendown()

    turtle.forward(SIZE)
    turtle.left(90)
    turtle.forward(SIZE / 2)
    turtle.left(90)
    turtle.forward(SIZE)
    turtle.right(90)
    turtle.forward(SIZE / 2)
    turtle.right(90)
    turtle.forward(SIZE)

    # leave turtle as we found it
    turtle.penup()
    turtle.setposition(position)

characters = {
    'O': draw_O,
    'S': draw_S,
    }

screen = Screen()
yertle = Turtle()

string = input()

for character in string:
    if character in characters:
        characters[character](yertle)
    yertle.forward(SIZE * 1.25)

screen.exitonclick()
