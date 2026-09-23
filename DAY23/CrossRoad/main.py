"""main"""
import time
# import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

# car_freq = 10
# level_no = 0
# x = 2

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()


    if player.ycor() == 280:
        player.goto(0, -280)
        score.update_level()
        cars.inc_speed()

    #     level_no += 1
    #     print("level_no:", level_no)
    #
    # if level_no == 5:m
    #     car_freq -= 3
    #     print(car_freq)
    # elif level_no == 10:
    #     car_freq -= 2
    # elif level_no == (10+x):
    #     car_freq -= 1
    #     x += 2

    # if level_no == 8:
    #     print(f"The {car_freq}")
    # if level_no == 18:
    #     print("new", car_freq)

    for i in cars.car_list:
        if i.distance(player) < 25:
            score.game_over()
            game_is_on = False


screen.exitonclick()