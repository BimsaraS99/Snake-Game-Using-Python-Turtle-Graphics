from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
import socket

SERVER = socket.gethostbyname(socket.gethostname())
SPEED = 10  # 1000 = 10ms
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.bgpic("image.gif")
screen.title("Snake Game")
screen.listen()


snake = Snake(3, (1, 0), (0, 0))  # start length, start moving direction, speed
food = Food()
score = Score()

food.display_food("square", "yellow")
snake.snake_create("square", "grey10")
time.sleep(1)  # one sec delay


def snake_eat_food():
    if snake.snake_head_position == food.food_position:
        return True
    return False


def exit_game():
    exit()


def restart_game():
    screen.tracer(0)
    score.restart_score()
    snake.restart_snake()
    food.restart_food()
    screen.tracer(1)
    time.sleep(1)
    main_function()


def main_function():
    print(snake.is_snake_out())
    while not snake.is_snake_out():
        snake.snake_move()
        if snake_eat_food():
            food.create_new_food()
            snake.increase_length_snake()
            score.increasing_mark(1)

        screen.onkey(snake.move_up, "w")
        screen.onkey(snake.move_down, "s")
        screen.onkey(snake.move_right, "d")
        screen.onkey(snake.move_left, "a")
        time.sleep(0.1)

    score.game_over()
    time.sleep(1.5)
    restart_game()


print(SERVER)
main_function()
screen.exitonclick()
