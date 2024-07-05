from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.shape("square")
        self.shapesize(stretch_len=10, stretch_wid=1, outline=2)
        self.goto(0,260)
        self.color("Pink")
        # self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        with open("data.txt" , mode = "r") as file:
            h_score = file.read()
        self.write(f"Score: {self.score}    High Score:  {h_score}", align="center", font=("Arial", 20, "normal"))
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as h_score:
                h_score.write(f"{self.score}")
        self.score = 0
        self.update_score()
        
    def increase_point(self):
        self.score += 1 
        self.update_score()