from turtle import Turtle
import random

colors=["red", "light blue", "blue", "yellow", "pink"]

class CarList(Turtle):

    def __init__(self):

        self.car_list=[]
        self.starting_dist=10
    
    def create_cars(self):

        random_choice=random.randint(1,5)
        if (random_choice==1):
            t=Turtle()
            t.shape("square")
            t.color(random.choice(colors))
            t.shapesize(stretch_wid=1, stretch_len=3)
            t.penup()
            t.setheading(180)
            t.speed("fast")
            t.goto(400, random.randint(-200,200))
            self.car_list.append(t)
        

    def move_cars(self):

        for i in self.car_list:
            if(i.xcor()>-450):
                i.forward(self.starting_dist)

    def increase_distance(self):

        self.starting_dist+=10
  
