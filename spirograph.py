import turtle
import random

tim = turtle.Turtle()
tim.shape('triangle')
tim.width(2)
colours = ["DarkOrchid", "IndianRed", "pink", "cyan", "green", "yellow", "red", "coral"]


def draw_shape(sides):
    for i in range(side):
        angle = 360 / side
        tim.forward(50)
        tim.left(angle)


for side in range(3, 11):
    draw_shape(side)
    tim.color(random.choice(colours))

screen = turtle.Screen()
screen.exitonclick()

