"""player"""
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    """tplayer"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """move_player"""
        if self.ycor() < FINISH_LINE_Y:
            new_y_cor = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y_cor)
