from insta_bot import InstaFollower

CHROME_DRIVER_PATH = 'D:/01.PROJECTS/100 Days of Code/DAY 45-52 Web Scraping, BS4, Selenium/Day52 Instagram Follower Bot/chromedriver.exe'


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
