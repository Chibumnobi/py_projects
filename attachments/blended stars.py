from turtle import *
from random import *
bgcolor('brown')
colormode(255)

col = ['white', 'grey', 'black']
speed(8)
for l in range(100):
    pu()
    x = randint(-300,300)
    y = randint(-300,300)
    goto(x,y)
    colo = choice(col)
    color(colo)
    pd()
    for s in range(5):
        fd(50)
        rt(144)

done()