from turtle import Turtle , Screen
import random as r

# Turtle.colormode(255)
mbappe = Turtle()
directions = [0, 90, 180, 270]
mbappe.speed(10)
mbappe.pensize(19)
for _ in range(200):
    mbappe.color(r.random(), r.random(), r.random())
    mbappe.forward(30)
    mbappe.setheading(r.choice(directions))
