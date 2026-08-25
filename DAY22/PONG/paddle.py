from turtle import Turtle

UP = 90
DOWN = 270
INIT_POSITIONS = [(-350,300),(-350,280),(-350,260),(-350,240),(-350,220)]
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_body = []
        self.create_paddle()
        self.head = self.paddle_body[0]
        self.tail = self.paddle_body[len(INIT_POSITIONS)-1]

    def create_paddle(self):
        for position in INIT_POSITIONS:
            self.add_paddle(position)

    def add_paddle(self, position):
        paddle = Turtle()
        paddle.penup()
        paddle.color("white")
        paddle.shape("square")
        paddle.width = 20
        paddle.goto(position)
        self.paddle_body.append(paddle)


    def up(self):
        if self.head.ycor() < 300:
            for paddle in self.paddle_body:
                paddle.setheading(UP)
                paddle.forward(MOVE_DISTANCE)
    def down(self):
        if self.tail.ycor() > -280:
            for paddle in self.paddle_body:
                paddle.setheading(DOWN)
                paddle.forward(MOVE_DISTANCE)