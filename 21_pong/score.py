from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align= "center", font=("Courier", 60, "normal"))

    def left_point(self):
        self.score_left += 1
        self.update_score()

    def right_point(self):
        self.score_right += 1
        self.update_score()
