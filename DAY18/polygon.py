from turtle import Turtle, Screen

tim = Turtle()
tim.penup()
tim.goto(-75, +60)
tim.pendown()

def triangle():
    for t in range(3):
        tim.color("red")
        tim.forward(75)
        tim.right(120)

def square():
    for t in range(4):
        tim.color("green")
        tim.forward(75)
        tim.right(90)

def pentagon():
    for t in range(5):
        tim.color("lightblue")
        tim.forward(75)
        tim.right(72)

def hexagon():
    for t in range(6):
        tim.color("lightgreen")
        tim.forward(75)
        tim.right(60)

def heptagon():
    for t in range(7):
        tim.color("pink")
        tim.forward(75)
        tim.right(51.4285)

def octagon():
    for t in range(8):
        tim.color("violet")
        tim.forward(75)
        tim.right(45)

def nonagon():
    for t in range(9):
        tim.color("slateblue2")
        tim.forward(75)
        tim.right(40)

def decagon():
    for t in range(10):
        tim.color("purple")
        tim.forward(75)
        tim.right(36)

square()
triangle()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

tom = Turtle()
tom.penup()
tom.goto(-75, +60)
tom.pendown()
color = ["red","green","lightblue","lightgreen","pink","violet","slateblue2","purple"]

num_of_sides = 3
color_number = 0
while num_of_sides <= 10:
    for i in range(num_of_sides):
        tom.color(color[color_number])
        angle = 360 / num_of_sides
        tom.forward(75)
        tom.left(angle)
    num_of_sides += 1
    color_number += 1



screen = Screen()
screen.exitonclick()