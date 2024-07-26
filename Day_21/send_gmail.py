import smtplib
import ssl
my_email = "randomnepali07@gmail.com"
my_pass = "jwmdakexukgvdvu"
receiver_email = "mailofreceiver@gmail.com"
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context= context) as connection:

    connection.login(user = my_email , password= my_pass)
    connection.sendmail(from_addr=my_email , 
                        to_addrs=receiver_email ,
                        msg="Subject:SEE THIS\n\nHello everyone")


