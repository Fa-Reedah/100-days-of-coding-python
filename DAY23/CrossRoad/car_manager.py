"""car"""
from turtle import Turtle
import random

COLORS = ["red", "orange", "brown", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5



class CarManager:
    """_car_manager_"""
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self, x=320):
        """_Create_car_"""
        if random.randint(1, 6) == 1:
            car = Turtle()  # create car
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.penup()
            car.goto(x, random.randint(-240, 240))
            self.car_list.append(car)

    def move(self):
        """Move_car"""
        for c in self.car_list:
            c.forward(self.car_speed)
            if c.xcor() < -320:
                self.car_list.remove(c)
                c.hideturtle()

    def inc_speed(self):
       self.car_speed += MOVE_INCREMENT
