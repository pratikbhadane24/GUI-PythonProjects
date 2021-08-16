from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
from time import sleep

gamescr = Screen()
gamescr.title("The Snake Game")
gamescr.setup(height=600, width=600)
gamescr.bgcolor("black")
gamescr.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

gamescr.listen()
gamescr.onkey(fun=snake.up, key="Up")
gamescr.onkey(fun=snake.down, key="Down")
gamescr.onkey(fun=snake.left, key="Left")
gamescr.onkey(fun=snake.right, key="Right")

game_on = True


while game_on:
    gamescr.update()
    sleep(0.05)

    snake.move()

# When our Snake eats the food 
    if snake.head.distance(food) < 15:
        food.newfoodloc()
        snake.snake_extend()
        scoreboard.increase_score()

# When Snake hits the walls
    if snake.head.xcor() > 289 or snake.head.xcor() < -289 or snake.head.ycor() > 289 or snake.head.ycor()< -289:
        scoreboard.reset()
        snake.reset()   

# When Snake hits his body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    


gamescr.exitonclick()
