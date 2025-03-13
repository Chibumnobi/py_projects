from turtle import *
from random import *

def cheese_ball(size):
    color('red')
    dot(size)
    color('orange')
    dot(size - 40)
    color('yellow')
    dot(size - 80)

for r in range(100):
    x = randint(-320, 320)
    y = randint(-320, 320)
    pu()
    goto(x,y)
    ball_size = randint(90, 140)
    pd()
    cheese_ball(ball_size)
done()