from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = 'python.scripting'
USERNAME = 'YOUR INSTA USERNAME'
PASSWORD = 'INSTA PASSWORD'



class InstaFollower():
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.base_window = self.driver.window_handles[0]

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        username = WebDriverWait(
            self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_area = self.driver.find_element_by_name('password')
        username.send_keys(USERNAME)
        password_area.send_keys(PASSWORD)
        time.sleep(2)
        password_area.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/python.scripting/followers/')
        time.sleep(3)
        followers_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]').click()
        time.sleep(1)
        self.dialog = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

        for i in range(10):
        # The modal in this case, becomes the arguments[0] in the script.
        # using Javascript: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.dialog)
            time.sleep(2)

    def follow(self):
        follow_btns = self.driver.find_elements_by_css_selector('li button')
        for btn in follow_btns:
            try:
                btn.click()
                time.sleep(2)
                print("Follow requested")

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                print("Already follow requested")

