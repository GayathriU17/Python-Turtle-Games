from gameturtle import GameTurtle
from turtle import Screen
from cars import Car
import random
import time

t=GameTurtle()
s=Screen()
s.bgcolor("white")
s.setup(width=800, height=600)

s.tracer(0)
list_of_cars=[]
for i in range(random.randint(2,10)):
    c=Car()
    c.create_car()
    list_of_cars.append(c)

is_game_on=True

while(is_game_on==True):
    for i in list_of_cars: 
        #time.sleep(0.2)
        s.update()
        i.move_car()
    
    









s.exitonclick()