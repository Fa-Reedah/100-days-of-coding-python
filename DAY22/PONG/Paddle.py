from turtle import Turtle


#INIT_POSITION1 = (350,0)
MOVE_DISTANCE = 25
class Paddle(Turtle):
    def __init__(self,init_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(init_position)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)


