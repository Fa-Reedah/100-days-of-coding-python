from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

def finis_line(colour):
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.color(colour)
    finish_line.width(5)
    finish_line.penup()
    finish_line.goto(150.5, 250)
    finish_line.pendown()
    finish_line.right(90)
    finish_line.fd(450)



start_race = False

user_guess = screen. textinput(title="Make Your Guess", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "cyan", "green", "blue", "purple"]

while not user_guess:
    user_guess = screen.textinput(title="Make Your Guess", prompt="Which turtle will win the race? Enter a color: ")
else:
    start_race = True

print(user_guess)
print(start_race)
finis_line("black")

start_x = -230
start_y = -100
end_x = 130

turtles = []
for t in range(0,6):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.shape("turtle")
    turtle.width(3)
    turtles.append(turtle)

n=0
for i in colors:
    turtles[n].color(colors[n])
    turtles[n].penup()
    turtles[n].goto(start_x, start_y)
    turtles[n].showturtle()
    n += 1
    start_y += 50

winner = ()
while start_race:
    for t in turtles:
        spd = random.randint(0,10)
        t.fd(spd)
        if t.xcor() >= end_x:
            start_race = False
            winner = t.pencolor()
            finis_line(winner)
            break


if user_guess.lower() == winner:
    print(f"You win.")
    print(f"{winner.capitalize()} turtle is the winner!")
else:
    print("You lost")
    print(f"{winner.capitalize()} turtle is the winner!")

screen.exitonclick()