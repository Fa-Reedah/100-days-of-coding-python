from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
COLOR = "white"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.goto(0,270)
        self.color(COLOR)
        self.hideturtle ()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align=ALIGNMENT, font=FONT)