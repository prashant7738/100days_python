from turtle import Turtle, Screen

mb = Turtle()
def move_forwards():
    mb.forward(10)

def move_backwards():
    mb.backward(10)

def turn_left():
    mb.left(20)

def turn_right():
    mb.right(20)

def clear():
    mb.clear()
    mb.penup()
    mb.home()
    mb.pendown()

screen = Screen()
screen.listen()
mb.speed = 0

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun =turn_right)

screen.onkey(key="c", fun=clear)
screen.exitonclick()

