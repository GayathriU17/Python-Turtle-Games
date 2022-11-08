from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self):

        super().__init__()
    
        
    def create_car(self):
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.setheading(180)
        self.goto(400, random.randint(-250,250))
        

    def move_car(self):
        #new_x=self.xcor()-10
        #new_y=self.ycor()
        #self.goto(new_x,new_y)
        if(self.xcor()>-400):
            self.forward(10)
