from turtle import Turtle
FILE_EASY_MODE = open("Easy_Game_High_Score.txt")
FILE_HARD_MODE = open("Hard_Game_High_Score.txt")


class Score(Turtle):
    def __init__(self, HScore):
        super().__init__()
        self.score = 0
        self.high_score = int(HScore)
        self.penup()
        self.color("white")
        self.goto(0, 365)
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def reset_game(self, mode):
        if self.score > self.high_score:
            self.high_score = self.score
            if mode == "hard":
                with open("Hard_Game_High_Score.txt", mode="w") as data:
                    data.write(f"{self.high_score}")
            elif mode == "easy":
                with open("Easy_Game_High_Score.txt", mode="w") as data:
                    data.write(f"{self.high_score}")
            self.score = 0
            self.clear()
            self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
    #     self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))

