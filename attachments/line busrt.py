import turtle
import random

turtle.bgcolor('black')
turtle.speed(0)
turtle.width(6)
paint = ['red','orange','yellow','green','blue']

for r in range(100):
    turtle.goto(0,0)
    angle = random.randint(0,360)
    length = random.randint(150,250)
    turtle.color(random.choice(paint))
    turtle.seth(angle)
    turtle.forward(length)