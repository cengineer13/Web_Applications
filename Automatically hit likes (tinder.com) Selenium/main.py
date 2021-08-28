from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

FB_USERNAME = "Your fb username"
FB_PASS = "Your fb password"

chrome_driver = "D:/01.PROJECTS/100 Days of Code/DAY 45-52 Web Scraping, BS4, Selenium/Day50 Tinder web scraping/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get("https://tinder.com/")


login_btn = driver.find_element_by_xpath('//*[@id="t812761606"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()
time.sleep(3)

login_block = driver.find_element_by_id("t812761606")
if login_block.get_attribute("aria-hidden") == "true":
    fb_login = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()
    time.sleep(2)

#Switch to Facebook login window

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
login_field = driver.find_element_by_name("email")
login_field.send_keys(FB_USERNAME)
password_field = driver.find_element_by_name("pass")
password_field.send_keys(FB_PASS)
password_field.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(3)
#Dismiss all pop-up requests
coockie_accept = driver.find_element_by_xpath('//*[@id="t812761606"]/div/div[2]/div/div/div[1]/button')
coockie_accept.click()
time.sleep(2)

location_btn = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div/div/div[3]/button')
location_btn.click()
time.sleep(2)

notification_btn = driver.find_element_by_xpath('//*[@id="t-915619470"]/div/div/div/div/div[3]/button[2]')
notification_btn.click()
time.sleep(2)


#Hit like button and swipe automatically

#Tinder free account has 100 "Likes" per day.
for i in range(100):

    time.sleep(1)
    try:
        print("Liked")
        like_btn = driver.find_element_by_xpath(
            '//*[@id="t812761606"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_btn.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
