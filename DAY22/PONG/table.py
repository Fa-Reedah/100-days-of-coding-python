from turtle import Turtle
#TO CREATE PING PONG TABLE USING DOTTED LINES ACROSS SCREEN
class Table(Turtle):
    def __init__(self, coord, heading,length):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.width(3)
        self.penup()
        self.goto(coord)
        self.setheading(heading)

        for dot in range(int(length/20)):
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)
