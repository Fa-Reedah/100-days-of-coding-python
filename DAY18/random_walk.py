import turtle
from turtle import Turtle,Screen
import random
t = Turtle()
t.speed(3)
t.width(15)

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

direction = [90, 180, 270, 0]
# colors = ["cyan","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
random_color()
for i in range(200):
    t.color(random_color())
    t.setheading(random.choice(direction))
    t.forward(20)



screen = Screen()
screen.exitonclick()