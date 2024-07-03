from turtle import Turtle

FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__ (self):
        
        super(). __init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280 , 260)
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.update_score()
         

    def update_score(self):
        self.clear()
        self.write( f"Level is : {self.score}" , align="left" , font=FONT)



    def increase_level(self):
        self.score += 1
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!" , align="center" , font=FONT)
    

