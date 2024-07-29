# In this code I tried to get the location of iss using API

import requests
from datetime import datetime
import time
MY_LAT =27.664400
MY_LON = 85.318794

def is_iss_near():
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # To raise error we need to use following line of code
    response.raise_for_status()

    # To retreive data 
    data = response.json()

    # To get longitude and latitude of iss
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    # If night then To check if iss is near to our location
    if abs(MY_LAT-latitude) < 5 and abs(MY_LON - longitude) < 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted" : 0
    }
    response = requests.get(url = "https://api.sunrise-sunset.org/json" ,params= parameters )
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])
    current_time = datetime.now()

    # TO CHECK WHETHER THE TIME IS DAY OR NIGHT
    if sunrise > sunset:
        if current_time.hour > sunset and current_time.hour <sunrise:
            return True
        
    if sunset > sunrise:
        if not current_time.hour > sunrise and current_time.hour < sunset:
            return True


import smtplib
import ssl
my_email = "randomnepali07@gmail.com"
my_pass = "jwmdakexukgvdvu"
receiver_email = "mailofreceiver@gmail.com"
context = ssl.create_default_context()
# TO CHECK BOTH CONDITION
while True:
    time.sleep(60)
    if is_iss_near() == True and is_night() == True:

        with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context= context) as connection:

            connection.login(user = my_email , password= my_pass)
            connection.sendmail(from_addr=my_email , 
                                to_addrs=receiver_email ,
                                msg="Subject:LOOK AT SKY \n\nHello ISS reaches at your sky")
