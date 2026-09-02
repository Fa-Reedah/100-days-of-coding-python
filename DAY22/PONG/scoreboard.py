from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color(COLOR)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 210)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(50, 210)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def right_score(self):
        self.r_score += 1
        self.update_score()
    def left_score(self):
        self.l_score += 1
        self.update_score()

    def l_wins(self):
        self.goto(0, 0)
        self.write("LEFT WINS!", align=ALIGNMENT, font=FONT)

    def r_wins(self):
        self.goto(0, 0)
        self.write("RIGHT WINS!", align=ALIGNMENT, font=FONT)

