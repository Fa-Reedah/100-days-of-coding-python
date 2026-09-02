from turtle import Turtle

MOVE_DISTANCE = 10
MOVE_Y = 10

def out_ball():
    print("Ball Out")

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_Y
        self.move_speed = 0.1

#### M0VE BALL LEFT OR RIGHT
    def move_ball(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

####  BOUNCE BALL ON AXIS
    def bounce_ball_y(self):      ## BOUNCE ON collision with X axis
        self.y_move *= -1
    def bounce_ball_x(self):     ##  BOUNCE ON collision with Y axis
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_ball_x()
        self.move_speed = 0.1
