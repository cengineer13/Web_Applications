import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "murodild@gmail.com"
MY_LAT = 37.566536  # Seoul
MY_LONG = 126.977966  # Seoul


def near_position(MY_LAT, MY_LONG):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude - 5 <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if near_position(MY_LAT, MY_LONG) and is_night():
        # and it is currently dark
        # Then send me an email to tell me to look up.
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user="mirodiljon.dusmatov@gmail.com", password="@Cengineer13")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="murodild@gmail.com",
                            msg="Subject:Look up")
        connection.close()
# BONUS: run the code every 60 seconds.
