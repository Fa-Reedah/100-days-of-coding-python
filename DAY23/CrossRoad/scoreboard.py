"""scoreboard"""
from turtle import Turtle
FONT = ("Courier", 24, "normal")
COLOR = "black"
GAME_OVER = ("Courier", 60, "normal")

class Scoreboard(Turtle):
    """record score"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.color(COLOR)
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=GAME_OVER)

