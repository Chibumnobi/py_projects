from turtle import *
from random import *
bgcolor('black')
pu()
rt(180)
fd(700)
lt(180)
col = ['red', 'gold', 'blue']
for chichi in range(15):
    color(choice(col))
    dot(100)
    fd(100)


done()