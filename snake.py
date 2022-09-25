from turtle import Turtle, Screen
from random import randint
screen = Screen()
snake_body = []  # objects
OUT_LIMIT = 299


class Snake:
    def __init__(self, len_start, direction_start, staring_position):
        """class snake, create a snake here"""
        self.len_snake = len_start
        self.move_direction = direction_start  # left-(-1,0) | right-(1,0) | up-(0,1) | down-(0,-1) | stop-(0,0)
        self.snake_head_position = staring_position
        self.snake_block_positions = [staring_position]
        self.start = staring_position
        self.shape = ""
        self.color = ""

    def snake_create(self, shape, color):
        screen.tracer(0)
        for position in range(self.len_snake):
            snake_body.append(Turtle(shape))
            self.shape, self.color = shape, color
            snake_body[-1].color(color)
            snake_body[-1].shapesize(stretch_len=0.9, stretch_wid=0.9)
            snake_body[-1].penup()
            snake_body[-1].goto(self.snake_block_positions[-1])
            snake_body[-1].speed('fastest')
            tup = ((self.snake_block_positions[-1][0] - 20), self.snake_block_positions[-1][1])
            self.snake_block_positions.append(tup)
        del self.snake_block_positions[-1]
        screen.tracer(1)
        return None

    def snake_move(self):
        distance = 20
        screen.tracer(0)
        for index in range(len(self.snake_block_positions)-1, 0, -1):
            self.snake_block_positions[index], self.snake_block_positions[index-1] = \
                self.snake_block_positions[index-1], self.snake_block_positions[index]

        x = self.snake_block_positions[1][0] + (distance * self.move_direction[0])
        y = self.snake_block_positions[1][1] + (distance * self.move_direction[1])
        self.snake_block_positions[0] = (x, y)
        for index, position in enumerate(self.snake_block_positions):
            snake_body[index].goto(position)
        self.snake_head_position = self.snake_block_positions[0]
        screen.tracer(1)
        return None

    def increase_length_snake(self):
        screen.tracer(0)
        snake_body.append(Turtle(self.shape))
        snake_body[-1].color(self.color)
        snake_body[-1].shapesize(stretch_len=0.9, stretch_wid=0.9)
        snake_body[-1].penup()
        tup = self.snake_block_positions[-1]
        self.snake_block_positions.append(tup)
        snake_body[-1].goto(tup)
        snake_body[-1].speed('fastest')

    def is_snake_out(self):
        head_x = self.snake_block_positions[0][0]
        head_y = self.snake_block_positions[0][1]
        if (head_x > OUT_LIMIT or head_x < -OUT_LIMIT) or (head_y > OUT_LIMIT or head_y < -OUT_LIMIT):
            self.move_direction = (0, 0)
            return True

        for index, position in enumerate(self.snake_block_positions):
            if index != 0 and self.snake_head_position == position:
                return True
        return False

    def restart_snake(self):
        for block in snake_body:
            block.goto(1000, 1000)
        snake_body.clear()
        self.snake_block_positions.clear()
        self.snake_block_positions = [self.start]
        self.move_direction = (1, 0)
        self.snake_create(self.shape, self.color)

    def move_up(self):
        if self.move_direction[1] != -1:
            self.move_direction = (0, 1)
        return None

    def move_down(self):
        if self.move_direction[1] != 1:
            self.move_direction = (0, -1)
        return None

    def move_left(self):
        if self.move_direction[0] != 1:
            self.move_direction = (-1, 0)
        return None

    def move_right(self):
        if self.move_direction[0] != -1:
            self.move_direction = (1, 0)
        return None
