from turtle import *
from random import randint

# Set up the turtle
speed(0)  # Fastest speed to draw quickly

width(9)
for m in range(36):
    for x in range(4):
        for l in range(1):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)

            # Set the turtle color using the RGB values
            colormode(255)  # Use 255 color mode for RGB
            pencolor(r, g, b)  # Set the pen color to the random RGB color

            # Move the turtle forward
            forward(100)
        right(90)
    right(10)

# Finish drawing
done()

