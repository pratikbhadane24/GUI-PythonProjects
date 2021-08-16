from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto_starting_positioin()
        self.moveUp()

    def moveUp(self):
        """Moves the player by some provided distance."""
        self.forward(MOVE_DISTANCE)

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_starting_positioin(self):
        self.goto(STARTING_POSITION)