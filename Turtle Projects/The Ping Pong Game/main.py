from turtle import Turtle, Screen, color, xcor
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

gamescr = Screen()
gamescr.title("The Pong Game")
gamescr.setup(height=600, width=800)
gamescr.bgcolor("black")
gamescr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Score()


gamescr.listen()
gamescr.onkey(fun=r_paddle.moveUp, key="Up")
gamescr.onkey(fun=r_paddle.moveDown, key="Down")
gamescr.onkey(fun=l_paddle.moveUp, key="w")
gamescr.onkey(fun=l_paddle.moveDown, key="s")

game_on = True
while game_on: 
    time.sleep(ball.move_speed)
    gamescr.update()
    ball.move()

# Bounce the ball
    # Bouncing on Wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_wall()
    # Bouncing on Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_paddle()

    # If miss by R_paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # If miss by L_paddle
    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.r_point()


gamescr.exitonclick()
