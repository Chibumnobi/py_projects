from turtle import *

bgcolor('black')
speed(0)
colormode(255)
width(1)

for n in range(255):
    color(255,255-n,n)
    fd(n)
    lt(91)
done()