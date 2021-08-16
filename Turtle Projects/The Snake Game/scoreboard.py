from turtle import Turtle, goto, update
import turtle

ALIGN = "center"
FONT = ("Fira Code", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0     
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")   
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align=ALIGN ,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0     
        self.updatescoreboard()
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", align=ALIGN ,font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.updatescoreboard()
