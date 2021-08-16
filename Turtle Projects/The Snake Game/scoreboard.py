from turtle import Turtle, goto, update
import turtle

ALIGN = "center"
FONT = ("Fira Code", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0     
        self.color("white")   
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN ,font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGN ,font=FONT)
        

    def increse_score(self):
        self.score += 1
        self.clear()
        self.updatescoreboard()
