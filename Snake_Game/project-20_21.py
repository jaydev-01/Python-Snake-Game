import time
from turtle import Screen
from snake_class import Snake
from food_of_snake import Food
from Score_Board import Score


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Nagin Game")
screen.tracer(0)
snake_size = 10
HS = 0

game_mode = screen.textinput(title="Game Mode", prompt="Enter Game Mode from the below:\n1.HARD\n2.EASY").lower()
snake = Snake()
food = Food()
if game_mode == "hard":
    with open("Hard_Game_High_Score.txt", mode="r") as data:
        HS = data.read()
elif game_mode == "easy":
    with open("Easy_Game_High_Score.txt", mode="r") as data:
        HS = data.read()

score = Score(HS)
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    if game_mode == "hard":
        if snake.hard_game():
            # game_is_on = False
            snake.reset_snake()
            score.reset_game(game_mode)
    elif game_mode == "easy":
        snake.easy_game()
    else:
        game_mode = screen.textinput(title="Wrong input", prompt="Enter Game Mode from the below:\n1.HARD\n2.EASY").lower()

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.increase_snake_size()

    if snake.self_collision():
        snake.reset_snake()
        score.reset_game(game_mode)

screen.exitonclick()
