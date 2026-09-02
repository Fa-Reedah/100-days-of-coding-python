from turtle import Screen
import time

from table import Table
from  Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#Create Screen
screen = Screen()
screen.setup(width=830,height=630) #screen inc by 10 to show table horizontal and vertical lines
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

#Create Pong Table
mid_vert_table = Table((0,300), 270, 600)
left_vert_table = Table((-400,300), 270, 600)
right_vert_table = Table((400,300), 270, 600)
#horiz
up_horiz_table = Table((-400,300), 0, 800)
down_horiz_table = Table((-400,-300),0, 800)


#Create Paddle
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
#Move paddle with keys
screen.listen()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")
#Create Ball
ball = Ball()
#Create Scoreboard
score = Scoreboard()


#Start game
start_game = True
while start_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #Detect Ball Collision with horizontal wall
    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce_ball_y()

    #Detect Ball touches paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()


    #Detect Ball misses right paddle
    if ball.xcor() > 380:
        score.left_score()
        ball.reset_ball()

    #Detect Ball misses left paddle
    if ball.xcor() < -380:
        score.right_score()
        ball.reset_ball()

    #YOU WIN
    if score.l_score >= 11 and score.r_score <= score.l_score + 2:
        score.l_wins()
        start_game = False
    elif score.r_score >= 11 and score.l_score <= score.r_score + 2:
        score.r_wins()

screen.exitonclick()