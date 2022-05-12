import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(1)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x = 20
        self.y = 20
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce(self):
        self.y *= -1
        self.move_speed *= 0.9

    def bounce_from_paddle(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.color("black")
        self.goto(0, 0)
        self.bounce_from_paddle()
        self.color("white")
        time.sleep(1)



