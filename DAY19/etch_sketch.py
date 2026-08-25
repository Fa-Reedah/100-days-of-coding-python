## functions that accepts other functions as input

#Etch-sketch App

from turtle import Screen, Turtle
tim = Turtle()

def fd():
    tim.fd(10)

def bk():
    tim.back(10)

def anti_clock():
    tim.left(10)

def clock():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.setheading(0)
    #tim.goto(0,0)
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()

screen.onkey(fun=fd, key="w")
screen.onkey(fun=bk, key="s")
screen.onkey(fun=anti_clock, key="a")
screen.onkey(fun=clock, key="d")
screen.onkey(fun=clear, key="c")



screen.exitonclick()