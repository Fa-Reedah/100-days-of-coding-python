from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

def forward():
    tom.forward(10)

screen.listen()
screen.onkey(fun=forward, key="space")
screen.exitonclick()