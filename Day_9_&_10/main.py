from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
Snake = Snake()
Snake.create_snake()

food = Food()
score = Score()


# Lets make binding of keys
screen.onkey(Snake.up , "Up")
screen.onkey(Snake.down , "Down")
screen.onkey(Snake.left , "Left")
screen.onkey(Snake.right , "Right")

# Game Main Loop
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()
    
    # Detect collision with food

    if Snake.head.distance(food) < 20:
        food.refresh()
        score.update_score()
        Snake.extend()
    
    # Detect collision with wall
    if Snake.head.xcor() > 290 or Snake.head.xcor() < -290 or Snake.head.ycor() > 290 or Snake.head.ycor() < -290:
        is_on = False
        score.game_over()


    # Check the detection of snake head with any other segment of snake
    for segment in Snake.segment[1:]:
        if Snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()


screen.exitonclick()




