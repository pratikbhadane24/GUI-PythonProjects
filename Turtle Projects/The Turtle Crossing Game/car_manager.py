from random import choice, randint
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        """Creates a new car"""
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-240, 240)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def moveCars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT
