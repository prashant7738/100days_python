from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
Snake = Snake()
Snake.create_snake()


# Lets make binding of keys
screen.onkey(Snake.up , "Up")
screen.onkey(Snake.down , "Down")
screen.onkey(Snake.left , "Left")
screen.onkey(Snake.right , "Right")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()
    
    


        

screen.exitonclick()




