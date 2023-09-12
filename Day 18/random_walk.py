#Challenge 4 - Generate Random Walk
#from turtle import Turtle, Screen
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

#color_set = ['MediumPurple','MediumTurquoise','OliveDrab2','orange1','orchid','yellow','SteelBlue1','DarkBlue']
directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_set = (r, g, b)
    return color_set

for _ in range(200):
    timmy.shape('arrow')
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))




screen = t.Screen()
screen.exitonclick()