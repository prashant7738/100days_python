from turtle import Turtle, Screen
import random
screen = Screen()



screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for i in range(6):
    mb = Turtle(shape="turtle")
    mb.color(colors[i])
    mb.penup()
    mb.goto(x=-220, y=y_position[i])

    all_turtles.append(mb)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
    









screen.exitonclick()





