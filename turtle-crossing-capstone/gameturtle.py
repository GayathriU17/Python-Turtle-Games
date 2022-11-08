from turtle import Turtle

class GameTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.penup()
        self.goto(0,-250) 
        self.setheading(90)

    def refresh(self):
        self.goto(0,-250)

    def move_turtle(self):
        if (self.ycor()<300):
            self.forward(10) 
        #elif(self.ycor()==300):     
            #self.refresh()     

    def up(self):
        self.move_turtle()
