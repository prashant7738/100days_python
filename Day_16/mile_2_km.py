from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width = 300 , height= 200)
window.config(padx= 50 , pady= 50)


input = Entry(width = 10)
input.grid(row = 1 , column= 2)

text_1 = Label(text="Miles")
text_1.grid(row =1 , column= 3)

text_2 = Label(text="is equal to")
text_2.grid(row =2 , column=1)

text_3 = Label(text = "K.M.")
text_3.grid(row = 2 , column=3)

def button_on_click():
    mile = input.get()
    km = float(mile) * 1.609344
    out_put = Label(text= f"{km}")
    out_put.grid(row =2 , column=2)

my_button = Button (text = "CONVERT", command= button_on_click )
my_button.grid(row =3 , column = 2)

window.mainloop()