from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0 
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text = "00:00")
    my_label.config(text = "TIMER")
    mark_label.config(text = "")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if (reps % 8 == 0):
        count_down(long_break_sec)
        my_label.config(text= "LONG _ BREAK" , font = ("Arial" , 24 , "bold") , fg = GREEN )

    elif (reps % 2 ==0):
        count_down(short_break_sec)
        my_label.config(text= "SHORT _ BREAK" , font = ("Arial" , 24 , "bold") , fg = GREEN )

    else:
        count_down(work_sec)
        my_label.config(text= "WORK" , font = ("Arial" , 24 , "bold") , fg = RED )

    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = int(count / 60)
    second = count % 60 
    

    if second < 10:
        second = f"0{second}"


    canvas.itemconfig(timer_text , text= f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000 ,count_down , count-1)
    else:
        start_timer()
        for _ in range(int(reps/2)):
            mark_label.config(text = "✓")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady= 50 , bg = YELLOW)

canvas = Canvas(width =200 , height = 224 , bg= YELLOW , highlightthickness= 0)
tomato_img = PhotoImage(file = "tomato.png" )
canvas.create_image(100 ,112 ,image = tomato_img )
timer_text = canvas.create_text(104, 120 , text="00:00" , fill = "white" , font=(FONT_NAME , 35 , "bold"))
canvas.grid(row = 2, column = 2)

my_label = Label(text= "TITLE" , font = ("Arial" , 24 , "bold") , fg =RED , bg= YELLOW)
my_label.grid(row = 1 , column= 2)

start_button = Button(text ="Start" , command= start_timer , bg = YELLOW , highlightthickness=0)
start_button.grid(row = 3 , column = 1)

mark_label = Label(text= "" , font = ("Arial" , 24 , "bold") , fg = "black" , bg= YELLOW)
mark_label.grid(row = 4 , column = 2)

reset_button = Button(text ="Reset" ,command = reset_timer, bg=YELLOW , highlightthickness=0 )
reset_button.grid(row = 3 , column = 3)

window.mainloop()
