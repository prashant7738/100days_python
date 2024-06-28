from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.shape("square")
        self.shapesize(stretch_len=10, stretch_wid=1, outline=2)
        self.goto(0,260)
        self.color("blue")
        # self.penup()
        self.update_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.score += 1
