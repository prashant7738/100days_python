##################### Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
import ssl

my_email = "randomnepali07@gmail.com"
my_pass = "jwmdakexukgvdvu"


data = pandas.read_csv("Birthday wisher/birthdays.csv")
now = dt.datetime.now()
today_tuple = (now.month , now.day)
birthday_dict = {(data_row['month'] , data_row['day']):data_row for (index , data_row) in data.iterrows()}
# print(birthday_dict)

if (today_tuple in birthday_dict):
    birthday_person = birthday_dict[today_tuple]
    
    file_path= f"Birthday wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as fp:
        content = fp.read()
        content = content.replace("[NAME]" ,birthday_person['name'])

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context = context) as smtp:
        smtp.login(user = my_email , password= my_pass)
        smtp.sendmail(my_email , birthday_person['email'] , f"Subject:Happy Birthday\n\n{content}")



