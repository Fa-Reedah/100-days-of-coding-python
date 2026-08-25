from turtle import Turtle
#TO CREATE PING PONG TABLE USING DOTTED LINES ACROSS SCREEN
class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.width(3)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)

        for dot in range(30):
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)