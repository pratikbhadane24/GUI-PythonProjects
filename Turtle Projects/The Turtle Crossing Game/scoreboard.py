from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.currentlev = 1
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.currentlev}", align="center", font=(FONT))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)

    def increase_lev(self):
        self.currentlev += 1
        self.clear()
        self.updatescoreboard()
