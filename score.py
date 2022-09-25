from turtle import Turtle, Screen


class Score(Turtle):
    """controlling the score board here"""
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.color("black")
        self.penup()
        self.goto(230, 270)
        self.hideturtle()
        self.marks = -1
        self.h_marks = 0
        with open("data.txt") as data:
            self.h_marks = int(data.read())
        self.increasing_mark(1)

    def increasing_mark(self, how_much):
        self.clear()
        self.goto(280, 270)
        self.marks += how_much
        self.h_marks += 0
        self.write(f"Score : {self.marks}", align="right", font=("Arial", 14, "normal"))
        self.goto(280, 250)
        self.write(f"Highest : {self.h_marks}", align="right", font=("Arial", 12, "normal"))

    def game_over(self):
        self.screen.tracer(0)
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -30)
        self.write(f"FINAL SCORE : {self.marks}", align="center", font=("Arial", 16, "normal"))
        self.screen.tracer(1)
        if self.marks > self.h_marks:
            self.h_marks = self.marks
            with open("data.txt", "w") as data:
                data.write(f"{self.h_marks}")

    def restart_score(self):
        self.clear()
        self.marks = -1
        self.increasing_mark(1)
