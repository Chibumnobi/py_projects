import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
paint = ['red','orange','yellow','green','blue']
turtle.penup()
#random.uniform(0.5,2.5)
for n in range(350):
    x = random.randint(-320,320)
    y = random.randint(-320,320)
    turtle.color(random.choice(paint))
    size = random.randint(15,51)
    turtle.goto(x,y)
    turtle.dot(size)