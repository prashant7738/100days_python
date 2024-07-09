from tkinter import *

# for making screen / windows use Tk() class
window = Tk()
window.title("TITLE")
window.minsize(width=500 , height= 300)
window.config(padx= 20 , pady= 20)

def button_onclick():
    text  = input.get()
    my_label = Label(text = f"yo {text}")
    my_label.grid(row = 1 , column = 1)

# for button use Button() class
my_button = Button(text  = "click me" , command = button_onclick)
my_button.grid(row = 2 , column= 2)

# for text input use Entry() class
input = Entry(width= 20)
input.grid( row = 3 , column= 4)

def action():
    print("Do something")

button = Button(text="Another button", command=action)
button.grid(row = 1, column= 3)







window.mainloop()