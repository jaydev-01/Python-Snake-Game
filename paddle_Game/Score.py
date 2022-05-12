from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.r_ply_s = 0
        self.l_ply_s = 0
        self.goto(-100, 210)
        self.write(self.l_ply_s, align="center", font=("Arial", 64, "normal"))
        self.goto(100, 210)
        self.write(self.r_ply_s, align="center", font=("Arial", 64, "normal"))

    def increase_r_ply_s(self):
        self.clear()
        self.r_ply_s += 1
        self.goto(-100, 210)
        self.write(self.l_ply_s, align="center", font=("Arial", 64, "normal"))
        self.goto(100, 210)
        self.write(self.r_ply_s, align="center", font=("Arial", 64, "normal"))

    def increase_l_ply_s(self):
        self.clear()
        self.l_ply_s += 1
        self.goto(-100, 210)
        self.write(self.l_ply_s, align="center", font=("Arial", 64, "normal"))
        self.goto(100, 210)
        self.write(self.r_ply_s, align="center", font=("Arial", 64, "normal"))
