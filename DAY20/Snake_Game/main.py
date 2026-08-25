import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

start_x = 0
start_y = 0
snakes = []
for i in range (0,3):
    snake = Turtle("square")
    snake.speed(1)
    snake.color("white")
    snake.penup()
    snake.goto(start_x,start_y)
    start_x -= 20
    snakes.append(snake)

start_game = True
while start_game:
    screen.update()
    time.sleep(1)
    for i in range (len(snakes)-1,0,-1):
        screen.update()
        time.sleep(1)
        new_x_cor = snakes[i-1].xcor()
        new_y_cor = snakes[i-1].ycor()
        snakes[i].goto(new_x_cor,new_y_cor)
        snakes[i].forward(50)

    #turn left
    # snakes[0].left(90)
    # snakes[2].forward(20)
    # snakes[1].forward(20)
    # snakes[0].forward(20)
    #start_game = False


screen.exitonclick()