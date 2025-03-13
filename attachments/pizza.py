from turtle import *
from random import *
bgcolor('cyan')

colormode(255)
color(242,174,148)
dot(500)

color('red')
dot(390)

color('yellow')
dot(350)

for r in range(20):
    color('black')
    pu()
    seth(6*2)
    x = randint(-100,100)
    y = randint(-100,100)
    goto(x,y)
    pd()
    dot(20)

pu()
for r in range(8):
    goto(0,0)
    color('cyan')
    pd()
    left(45)
    fd(250)
done()