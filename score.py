from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(f"LEVEL {self.score}", font="Calibri", align="center")

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"LEVEL {self.score}", font="Calibri", align="center")
        print(self.score)