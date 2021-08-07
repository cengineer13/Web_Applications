import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import time

product_url = "https://www.amazon.com/GTPOFFICE-Computer-Reclining-Adjustable-Headrest/dp/B07SRXTQ8M"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/92.0.4515.131 Safari/537.36",
          "Accept-Language": "gzip, deflate"
          }


def amazon():
    response = requests.get(product_url, headers=header)

    web_page = response.text
    soup = BeautifulSoup(web_page, 'lxml')

    price = soup.find("span", id="priceblock_saleprice").text
    float_price = float(price.split("$")[1])

    return float_price


def send_email(price):
    if price > 90.0:
        my_password = input("Type your password and press enter: ")
        my_email = "mirodiljon.dusmatov@gmail.com"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs="murodild@gmail.com",
                            msg=f"Subject:Hot price!!!\n\n Hello boy! The product you "
                                f"want price was downed. See {price} and check this link below:\n {product_url}")

        connection.close()


while True:
    one_hour = 3600
    new_price = amazon()
    send_email(new_price)
    #Run again every 10 hours
    time.sleep(10 * one_hour)
