from turtle import *
from random import *

bgcolor('light blue')
colormode(255)
speed(10)

color(209,154,98)
dot(500)

color('pink')
dot(450)

color('light blue')
dot(250)

col = ['white','yellow','magenta']

width(10)
for s in range(60):
    seth(s*6)
    pu()
    goto(0,0)
    fd(randint(150,230))
    seth(randint(1,360))
    color(choice(col))
    pd()
    fd(32)

done()