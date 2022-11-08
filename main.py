from gameturtle import GameTurtle
from turtle import Screen, Turtle
from cars import CarList
import random
import time
from score import Score

t=GameTurtle()
s=Screen()
s.bgcolor("white")
s.setup(width=800, height=600)

s.tracer(0)

c=CarList()
sc=Score()
score=0
is_game_on=True

s.listen()
s.onkey(t.up, "Up")

while(is_game_on==True):
    c.create_cars()
    time.sleep(0.1)
    s.update()
    c.move_cars()

    if (t.ycor()==300):
        t.refresh()
        sc.update_score()
        c.increase_distance()
        
    
    for car in c.car_list:
        if (car.distance(t)<20):
            is_game_on=False
            screenturtle=Turtle()
            screenturtle.color("black")
            screenturtle.hideturtle()
            screenturtle.penup()
            screenturtle.write("GAME OVER", font="Calibri", align="center")
            screenturtle.goto(-50,0)

    

    
    









s.exitonclick()