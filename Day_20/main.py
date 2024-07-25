from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data=pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient= "records")
else:
    to_learn = data.to_dict(orient= "records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French" , fill = "black")
    canvas.itemconfig(card_word , text = current_card["French"] , fill = "black")
    canvas.itemconfig(card_background , image= card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "English" , fill = "white")
    canvas.itemconfig(card_word , text = current_card["English"] , fill = "white")
    canvas.itemconfig(card_background , image= card_back)

    
def learned():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    # print(len(new_data))
    new_data.to_csv("data/words_to_learn.csv" , index = False)

    next_card()


window = Tk()
flip_timer = window.after(3000, flip_card)
window.config(bg=BACKGROUND_COLOR , padx =60 , pady=60)
window.title("FLASHY")
canvas = Canvas(width = 600, height = 400)
card_front= PhotoImage(file ="images/card_front.png")
card_back= PhotoImage(file ="images/card_back.png")
card_background = canvas.create_image(300 ,200 ,image = card_front)
card_title = canvas.create_text(300 , 50 ,text="" ,font= ("Arial" , 40, "italic") )
card_word = canvas.create_text(300 , 250 ,text="" ,font= ("Arial" , 60 ,"bold") )
canvas.config(bg =BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0 , column=0 , columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image = cross_image, highlightthickness=0, command = next_card)
cross_button.grid(row = 1, column =0 )

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image = tick_image, highlightthickness= 0, command = learned)
tick_button.grid(row = 1 , column=1)

next_card()

window.mainloop()

