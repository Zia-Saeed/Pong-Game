from turtle import Turtle
INITIAL_POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.penup()
        self.shape("circle")
        self.color("blue")
        self.x_move = 10
        self.y_move = 10

    def initial_position(self):
        self.goto(INITIAL_POSITION)

    def move_to(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_to_left_player(self):
        self.x_move *= -1
        self.y_move *= -1
        self.initial_position()
        self.move_to()

    def move_to_right_player(self):
        self.x_move = 10
        self.y_move = 10
        self.initial_position()
        self.move_to()

    def bounce(self):
        self.y_move *= -1

    def collision_with_paddles(self):
        self.x_move *= -1






