import smtplib
import ssl
import datetime as dt
import random

now = dt.datetime.now()
day_week = now.weekday()

with open("gmail.txt") as fp:
    sender_mail_list = [list for list in fp]


for each in sender_mail_list:
    my_email = "randomnepali07@gmail.com"
    password = "jwmdakexukgvdvu"
    to_email = each

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context = context) as connection:
        connection.login(user=my_email, password=password)
        
        if (day_week == 0):
            with open("quotes.txt") as quote:
                list = [line for line in quote]
                random_quote = random.choice(list)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Monday Motivation \n\n{random_quote}"
            )
        else:
            print("Today is not day of monday motivation")







