from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
COLOR = "white"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.goto(0,270)
        self.color(COLOR)
        self.hideturtle ()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.update_score()
