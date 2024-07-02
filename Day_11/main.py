from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

def check_collision():
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()

def check_miss():
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        ball.speed_reset()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        ball.speed_reset()

def check_wall_collision():
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    ball.move()
    check_collision()
    check_miss()
    check_wall_collision()
    screen.update()

screen.exitonclick()

