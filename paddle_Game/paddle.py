from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(x, y)

    def up(self):
        if self.ycor() > 250:
            self.goto(self.xcor(), self.ycor() - 50)
        else:
            self.goto(self.xcor(), self.ycor()+10)

    def down(self):
        if self.ycor() < -250:
            self.goto(self.xcor(), self.ycor() + 50)
        else:
            self.goto(self.xcor(), self.ycor() - 10)


