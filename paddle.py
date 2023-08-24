from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=4.5, stretch_len=0.6)
        self.color("white")
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)


