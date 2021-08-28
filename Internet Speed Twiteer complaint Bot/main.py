from auto_tweet import InternetSpeedTwitterBot



chrome_driver_path = 'D:/01.PROJECTS/100 Days of Code/DAY 45-52 Web Scraping, ' \
                     'BS4, Selenium/Day51 Internet Speed Twiteer complaint Bot/chromedriver.exe'


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
