from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    from random import randint , choice , shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2,3))]
    password_symbols = [choice(symbols) for _ in range(randint(2,3))]


    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    new_password = "".join(password_list)
    
    pass_entry.insert( 0 , new_password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    web_name = web_entry.get()
    email_name = email_entry.get()
    password = pass_entry.get()

    if len(password)==0  or len(web_name) ==0 or len(email_name) == 0:
        messagebox.showinfo(title= "ERROR" , message="Please fill the Empty Bpxes")

    else:
        is_ok = messagebox.askokcancel(title = "IS IT oK?" , message=f"IS THIS OKAY? \n Website name : {web_name}  \n Email: {email_name}  \n Password : {password}")

        if is_ok:
            with open("data.txt" , "a") as data_file:
                data_file.write("\n")
                data_file.write(f"Website name : {web_name}  || Email: {email_name}  || Password : {password}")
                web_entry.delete(0 ,END)
                pass_entry.delete(0 , END)
                web_entry.focus()
                pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=30 , pady=30)
window.title("Password Manager")
logo_img = PhotoImage(file = "logo.png")
my_canvas = Canvas(height=200 , width= 200)
my_canvas.create_image(100 ,100 , image = logo_img)
my_canvas.grid(row = 0 , column= 1)

label1 = Label(text="Website :" )
label1.grid(row = 1 , column= 0)

label2= Label(text = "Email / Username :")
label2.grid(row = 2, column=0)

label3= Label(text = "Password :")
label3.grid(row = 3, column=0)

web_entry = Entry(width=36)
web_entry.grid(row =1 , column=1 ,columnspan=2)
web_entry.focus()

email_entry = Entry(width = 36)
email_entry.grid(row =2 , column=1 ,columnspan=2)
email_entry.insert(0 , "prashantkafle7738@gmail.com")

pass_entry = Entry(width = 21)
pass_entry.grid(row =3 , column=1)

gen_pass_button = Button(text="Generate" , command = generate_pass)
gen_pass_button.grid(row = 3, column = 2)

add_button = Button(text="ADD" , width=36, command = add_pass)
add_button.grid(row = 4 , column =1, columnspan=2)



window.mainloop()