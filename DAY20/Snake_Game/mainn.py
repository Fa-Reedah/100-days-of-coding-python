from turtle import Screen
import time

from food import Food
from snake import Snake
from scoreboard import Score
#CREATE SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Create snake body
snake = Snake()
# Create snake food
food = Food()
# Track Score
score = Score()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


# START GAME
start_game = True
while start_game:
    screen.update()
    time.sleep(0.1)
    #Create Snake

    #Move Snake
    snake.move_snake()

    #Detect snake head collision with food.
    if snake.head.distance(food) < 20:
        #add snake length
        snake.extend_snake()
        #Add score
        score.increase_score()
        #Refresh Food
        food.refresh_food()

    #Detect collision with wall
    #if head collides with near wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        #trigger reset
        snake.reset()
        score.reset_score()


    #Detect collision with tail
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            # trigger reset
            snake.reset()
            score.reset_score()
 

screen.exitonclick()