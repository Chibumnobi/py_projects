from turtle import *
from random import *
speed(7)

col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for x in range(-400,400,60):
    for y in range(-400,400,60):
        colour =choice(col)
        color(colour)
        pu()
        goto(x,y)
        pd()
        dot(20)
done()
