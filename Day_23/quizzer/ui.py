from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quiz_Ui:
    def __init__(self , quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx= 20 , pady= 20 , background=THEME_COLOR)
        self.window.title("Quizzler")
        self.canvas = Canvas(height = 250 , width= 300 , bg = "white")
        self.question_text = self.canvas.create_text(125,150, text ="Question", fill= "black" , font= ("Arial" ,16) ,width= 250)
        self.canvas.grid(row =1 , column= 0, columnspan=4)

        self.score_text = Label(text = "Score = 0" , font =('Arial' , 20 , 'italic') , bg=THEME_COLOR)
        self.score_text.grid(row = 0 , column=3)

        tick_img = PhotoImage(file = "images/true.png")
        self.tick_button = Button(image = tick_img , highlightthickness= 0 , command= self.true_pressed)
        self.tick_button.grid(row = 2, column = 1 , pady= 20 )

        cross_img = PhotoImage(file = "images/false.png")
        self.cross_button = Button(image = cross_img ,highlightthickness= 0, command = self.false_pressed)
        self.cross_button.grid(row = 2, column = 3 ,pady =20)

        self.next_question()
        self.window.mainloop()


    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text = q_text)
            self.score_text.config(text=f"Score = {self.quiz.score}")

        else:
           self.canvas.itemconfig(self.question_text , text = "You have finished your question")
           self.tick_button.config(state= "disabled")
           self.cross_button.config(state= "disabled")
    

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        
        if is_right == True:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000 , self.next_question)



    
