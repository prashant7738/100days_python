from turtle import Turtle
import random as r

mbappe_turtle = Turtle()

for n in range(3,11):
    for _ in range(n):
        mbappe_turtle.forward(100)
        mbappe_turtle.right(360/n)
    mbappe_turtle.color(r.random(), r.random(), r.random())


