from turtle import *
from random import *

speed(0)
shape('turtle')

coo = ['red','orange','yellow','green','blue']

for size in range(400,0,-10):
    color(choice(coo))
    dot(size)
done()