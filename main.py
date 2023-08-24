from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
L_SCORE = 0
R_SCORE = 0
L_SCORE_POSITION = (-80, 280)
R_SCORE_POSITION = (80, 280)
SLEEP_TIME = 0.1
if __name__ == '__main__':

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title("Pong")
    screen.tracer(0)

    l_paddle = Paddle((-390, 0))
    r_paddle = Paddle((380, 0))

    ball = Ball()

    l_score = Score(L_SCORE_POSITION, L_SCORE)
    r_score = Score(R_SCORE_POSITION, R_SCORE)

    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.move_up)
    screen.onkey(key="Down", fun=r_paddle.move_down)
    screen.onkey(key="w", fun=l_paddle.move_up)
    screen.onkey(key="s", fun=l_paddle.move_down)

    is_game_on = True
    while is_game_on:

        screen.update()
        ball.move_to()
        time.sleep(SLEEP_TIME)

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        # Detect collision with paddle
        if ball.distance(l_paddle) < 40 and ball.xcor() > -390:
            ball.collision_with_paddles()
            SLEEP_TIME *= 0.9

        elif ball.distance(r_paddle) < 50 and ball.xcor() > 350:
            ball.collision_with_paddles()
            SLEEP_TIME *= 0.9

        # Score check
        elif ball.xcor() > 400:
            l_score.increase_score()
            ball.move_to_left_player()
            SLEEP_TIME = 0.1

        elif ball.xcor() < -400:
            r_score.increase_score()
            ball.move_to_right_player()
            SLEEP_TIME = 0.1







    screen.exitonclick()
