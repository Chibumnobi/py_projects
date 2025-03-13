from turtle import *

speed(0)
colormode(255)
width(4)
for r in range(2):
    for x in range(0,100):
        goto(0,0)
        color(255,x,0)
        fd(300)
        right(2)
done()