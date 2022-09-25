import random
from turtle import Turtle, Screen
screen = Screen()


class Food:
    """making foods for snake"""
    def __init__(self):
        self.food_position = tuple()
        self.shape = ""
        self.color = ""
        self.food = Turtle()

    def display_food(self, shape, color):
        screen.tracer(0)
        self.shape, self.color = shape, color
        food = self.food
        food.penup()
        food.color(color)
        food.shape(shape)
        food.shapesize(stretch_len=0.6, stretch_wid=0.6)
        list1 = list(range(-260, 260, 20))
        food_x, food_y = random.choice(list1), random.choice(list1)
        self.food_position = (food_x, food_y)
        food.goto(food_x, food_y)
        screen.tracer(1)
        return None

    def create_new_food(self):
        screen.tracer(0)
        list1 = list(range(-260, 260, 20))
        food_x, food_y = random.choice(list1), random.choice(list1)
        self.food_position = (food_x, food_y)
        self.food.goto(food_x, food_y)
        screen.tracer(1)

    def restart_food(self):
        self.create_new_food()

