from turtle import Turtle

# starting_pos = [(0, 0), (-20, 0), (-40, 0)]
starting_pos = [(0, 0), (-20, 0)]
moving_distance = 20


class Snake:
    def __init__ (self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for cord in starting_pos:
            self.add_segment(cord)
            

    def add_segment(self, position):
        mb = Turtle("square")
        mb.color("white")
        mb.penup()
        mb.goto(position)
        self.segment.append(mb)

    def extend(self):
         self.add_segment(self.segment[-1].position())
        


    def reset(self):
         for seg in self.segment:
              seg.goto(1000,1000)

         self.segment.clear()
         self.create_snake()
         self.head = self.segment[0]
              

    def move(self):
        for i in range(len(self.segment)-1 , 0 , -1):
                    x_cor = self.segment[i-1].xcor()
                    y_cor = self.segment[i-1].ycor()

                    self.segment[i].goto(x_cor, y_cor)

        self.segment[0].forward(moving_distance)


    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)


    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)


    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)


    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)



