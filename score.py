from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self, position, score):
        super().__init__()
        self.position = position
        self.score = score
        self.score_move()

    def score_move(self):
        self.goto(self.position)
        self.hideturtle()
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_move()






