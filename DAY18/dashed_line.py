from turtle import Turtle,Screen

timmy = Turtle()
timmy.penup()
timmy.goto(-600, 0)

for t in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()