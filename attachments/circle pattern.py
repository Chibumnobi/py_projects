import turtle
turtle.bgcolor('cyan')
import random

turtle.shape('turtle')

turtle.speed(0)

color = ['blue', 'red', 'green']

for i in range(36):
    for r in range(1):
        turtle.circle(90)
        turtle.color(random.choice(color))
    turtle.right(10)

for r in range(36):
    for r in range(1):
        turtle.circle(55)
        turtle.color(random.choice(color))
    turtle.right(10)

for l in range(36):
    for r in range(1):
        turtle.circle(35)
        turtle.color(random.choice(color))
    turtle.right(10)

turtle.pu()
turtle.fd(180)
turtle.lt(90)
turtle.fd(180)
turtle.lt(90)
turtle.pd()

for l in range(4):
    turtle.width(5)
    turtle.fd(360)
    turtle.lt(90)

turtle.done()