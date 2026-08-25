from turtle import Screen
import time

from table import Table
from paddle import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

#Create Pong Table
pong_table = Table()
#Create Paddle
paddle1 = Paddle()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

start_game = True
while start_game:
    screen.update()
    time.sleep(0.1)
    #Move paddle1






screen.exitonclick()