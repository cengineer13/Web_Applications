import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 10
TWITTER_LOGIN = "your twetter account"
TWITTER_PASSWORD = "your password"



class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedcheck.org/en')
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.ARROW_DOWN)
        html.send_keys(Keys.ARROW_DOWN)
        html.send_keys(Keys.ARROW_DOWN)
        time.sleep(5)
        speed_btn = self.driver.find_element_by_css_selector('.start-container a')
        speed_btn.click()
        time.sleep(60)

        # GET DOWN and UP scores
        self.down = self.driver.find_element_by_xpath(''
                                                 '//*[@id="app-container"]/angular-main/main/div/div/result/div/div['
                                                 '1]/div[1]/div[2]/div/div/div[1]/div/div[3]').text
        self.up = self.driver.find_element_by_xpath(''
                                          '//*[@id="app-container"]/angular-main/main/div/div/result/div/div[1]/div['
                                          '1]/div[3]/div/div/div[1]/div/div[3]').text
        print(self.up)
        print(self.down)
        time.sleep(5)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        login_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        login_field.send_keys(TWITTER_LOGIN)
        password_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password_field.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br')
        twit_complaint = f'Hey internet Provider. why my internet speed {self.down}/{self.up} when I pay 150down/10up?'
        tweet_compose.send_keys(twit_complaint)
        time.sleep(3)

        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()
        #Wait some time to load page
        time.sleep(2)
