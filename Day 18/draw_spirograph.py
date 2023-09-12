# challenge 5 - Draw a Spirograph

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_set = (r, g, b)
    return color_set


def draw_spirograph(size_of_gap):
    for i in range(int(360/ size_of_gap)):
        timmy.color(random_color())
        timmy.circle(80)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()