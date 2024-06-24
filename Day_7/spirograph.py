from turtle import Turtle , Screen
import random as r

screen = Screen()


mbappe = Turtle()
mbappe.speed("fastest")
def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        mbappe.color(r.random(), r.random(), r.random())
        mbappe.circle(100)
        initial_heading = mbappe.heading()
        mbappe.setheading(initial_heading+ gap)


draw_spirograph(7)

screen.exitonclick()