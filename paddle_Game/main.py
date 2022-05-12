import time
from turtle import Screen
from paddle import Paddle
from Ball import Ball
from Score import Score


game_is_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Peddle Game")


paddle1 = Paddle(370, 0)
paddle2 = Paddle(-375, 0)
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(key="w", fun=paddle2.up)
screen.onkeypress(key="s", fun=paddle2.down)
screen.onkeypress(key="o", fun=paddle1.up)
screen.onkeypress(key="k", fun=paddle1.down)

screen.tracer()

while game_is_on:
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 380:
        score.increase_l_ply_s()
        ball.reset_ball()

    elif ball.xcor() < -380:
        score.increase_r_ply_s()
        ball.reset_ball()

    if (ball.distance(paddle1) < 50 and ball.xcor() > 340) or (ball.distance(paddle2) < 50 and ball.xcor() < -340):
        ball.bounce_from_paddle()


screen.exitonclick()
