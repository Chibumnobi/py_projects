import turtle as john
import random 

color = ['red','green','blue','yellow','orange']

for n in range(100):
    john.color(random.choice(color))
    x = random.randint(-360,360)
    y = random.randint(-360,360)
    john.goto(x,y)
    john.dot(20)