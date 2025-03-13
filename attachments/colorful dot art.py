import turtle as john
import random 

color = ['red','green','blue','yellow','orange']
john.penup()
for n in range(100):
    size = random.randint(80, 360)
    john.color(random.choice(color))
    x = random.randint(-320,320)
    y = random.randint(-320,320)
    john.goto(x,y)
    john.dot(size)