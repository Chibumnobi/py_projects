from turtle import *
from random import randint
colormode(255)
speed(10)
bgcolor('black')

for z in range(100):
    r = randint(0,255)
    g = randint(0,255)
    x = randint(-320,-320)
    y = randint(-320,-320)
    for size in range(100,0,-1):
        color(r,g,size)
        dot(size)
    goto(x,y)
done()