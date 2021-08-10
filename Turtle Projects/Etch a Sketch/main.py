from turtle import Screen, Turtle, screensize


def movefd():
    tom.fd(10)


def movebk():
    tom.backward(10)


def moveright():
    tom.left(10)


def moveleft():
    tom.right(10)


def clrscr():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


tom = Turtle()
tom.speed(0)
screen = Screen()
screen.listen()
screen.onkey(fun=movefd, key="w")
screen.onkey(fun=movebk, key="s")
screen.onkey(fun=moveright, key="d")
screen.onkey(fun=moveleft, key="a")
screen.onkey(fun=clrscr, key="c")

screen.exitonclick()
