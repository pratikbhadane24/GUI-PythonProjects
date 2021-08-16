import time
from turtle import Screen, goto
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
levelscore = Scoreboard()

screen.listen()
screen.onkey(fun=player.moveUp, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.moveCars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            levelscore.gameover()
            game_is_on = False

    if player.is_at_finishline():
        player.goto_starting_positioin()
        car_manager.new_level()
        levelscore.increase_lev()

screen.exitonclick()
