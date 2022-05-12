from turtle import Turtle
move_distance = 20


class Snake:
    def __init__(self):
        self.staring_position = [(0, 0), (-20, 0), (-40, 0)]
        self.snake = []
        for pos in self.staring_position:
            snake_body_part = Turtle("square")
            snake_body_part.color("white")
            snake_body_part.penup()
            snake_body_part.goto(pos)
            self.snake.append(snake_body_part)
        self.head = self.snake[0]

    def move(self):
        for pos in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[pos - 1].xcor()
            new_y = self.snake[pos - 1].ycor()
            self.snake[pos].goto(new_x, new_y)
        self.snake[0].forward(move_distance)
        self.snake[len(self.snake) - 1].color("white")

    def up(self):
        if self.snake[0].heading() == 180 or self.snake[0].heading() == 0:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() == 180 or self.snake[0].heading() == 0:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() == 90 or self.snake[0].heading() == 270:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() == 90 or self.snake[0].heading() == 270:
            self.snake[0].setheading(0)

    def increase_snake_size(self):
        snake_body_part = Turtle("square")
        snake_body_part.penup()
        self.snake.append(snake_body_part)

    def self_collision(self):
        for self_part in self.snake[1:]:
            if self.head.distance(self_part) < 10:
                return 1

    def easy_game(self):
        if self.head.xcor() > 390:
            self.head.setx(-390)
        elif self.head.xcor() < -390:
            self.head.setx(390)
        elif self.head.ycor() > 360:
            self.head.sety(-390)
        elif self.head.ycor() < -390:
            self.head.sety(360)

    def hard_game(self):
        if self.head.xcor() > 390 or self.head.xcor() < -390 or self.head.ycor() > 360 or self.head.ycor() < -390:
            return 1

    def reset_snake(self):
        for bp in self.snake:
            bp.goto(1000, 1000)
        self.snake.clear()
        self.__init__()

