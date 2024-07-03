from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):

        super().__init__()
        
        self.color("black")
        self.shape("turtle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def is_reach_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


