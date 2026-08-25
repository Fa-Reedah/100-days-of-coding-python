from turtle import Turtle, Screen
timmy = Turtle()
def draw_a_square():
    timmy.forward(100)
    timmy.right(90)


for i in range(4):
    draw_a_square()


screen = Screen()
screen.exitonclick()

# import turtle as t
# tim = t.Turtle()
