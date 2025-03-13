from turtle import *

speed(0)
colormode(255)

for x in range(0,200):
    color(255,128,x)
    goto(x,0)
    goto(x,200)
done()