from random import choice
from turtle import Turtle, Screen
import turtle

color_list = [(213, 151, 106), (248, 247, 74), (87, 244, 200), (41, 12, 179), (224, 115, 161), (160, 10, 76), (17, 181, 76), (31, 6, 90), (223, 49, 138), (151, 88, 43), (118, 98, 228), (84, 34, 13), (9, 97, 45),
              (85, 6, 38), (183, 182, 241), (71, 216, 90), (178, 45, 104), (47, 16, 249), (34, 142, 47), (155, 134, 215), (173, 9, 7), (75, 244, 249), (228, 166, 205), (234, 47, 43), (87, 74, 148), (6, 96, 100)]

turtle.colormode(255)


tony = Turtle()
tony.speed("fastest")
tony.penup()
tony.hideturtle()
tony.setheading(225)
tony.fd(300)
tony.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tony.dot(20, choice(color_list))
    tony.fd(40)

    if dot_count % 10 == 0: 
        tony.left(90)
        tony.fd(40)
        tony.setheading(180)
        tony.fd(400)
        tony.setheading(0)

myScreen = Screen()
myScreen.exitonclick()