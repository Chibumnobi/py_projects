from turtle import *

bgcolor('black')
speed(10)
paint = ['red','orange','yellow','green','blue','purple']
colormode(255)


for n in range(255):
    color(paint[n%6])
    fd(n)
    lt(61)
done()