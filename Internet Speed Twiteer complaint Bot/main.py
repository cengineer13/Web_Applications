from auto_tweet import InternetSpeedTwitterBot



chrome_driver_path = 'path to chromedriver.exe'


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
