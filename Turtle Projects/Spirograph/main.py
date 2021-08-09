from random import randint
from turtle import Turtle, Screen
import turtle

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    mycolor = (r, g, b)
    return mycolor

turtle.colormode(255)
jim = Turtle()
jim.speed(0)

def draw_spirograh(gap_size):
    for _ in range(int(360/gap_size)):
        jim.color(random_color())
        current_heading = jim.heading()
        jim.setheading(current_heading + gap_size)
        jim.circle(100) 

draw_spirograh(3)


myscreen = Screen()
myscreen.exitonclick()