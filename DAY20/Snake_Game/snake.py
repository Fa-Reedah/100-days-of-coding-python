from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20
INIT_POSITIONS = [(0,0) , (-20,0) , (-40,0)]

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """Create the Snake object"""
        for position in INIT_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle()
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.width = 18
        snake.goto(position)
        self.snake_body.append(snake)

    def extend_snake(self):
        """Extend the Snake object after collision with food"""
        self.add_snake(self.snake_body[-1].position())


    def move_snake(self):
        """Move the snake forward"""
        for i in range((len(self.snake_body)-1), 0, -1):
            new_position_x = (self.snake_body[i-1].xcor())
            new_position_y = (self.snake_body[i-1].ycor())
            self.snake_body[i].goto(new_position_x, new_position_y)

        self.head.forward(MOVE_DISTANCE)


    def Up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)
        self.move_snake()
    def Down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)
        self.move_snake()
    def Left(self):
        if self.head.heading() !=  RIGHT :
            self.head.setheading(LEFT)
        self.move_snake()
    def Right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)
        self.move_snake()