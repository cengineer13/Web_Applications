import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from data import all_links, all_adress, all_prices

chrome_driver_path = "Link to chromedriver.exe"
GOOGLE_FORM_LINK = "Google form link"

driver = webdriver.Chrome(executable_path=chrome_driver_path)



for i in range(len(all_adress)):
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(2)

    address_field = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')


    ActionChains(driver).move_to_element(address_field).click().perform()
    address_field.send_keys(all_adress[i])
    time.sleep(1)

    ActionChains(driver).move_to_element(price_field).click().perform()
    price_field.send_keys(all_prices[i])
    time.sleep(1)

    ActionChains(driver).move_to_element(link_field).click().perform()
    link_field.send_keys(all_links[i])
    time.sleep(1)

    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit_btn.click()
    time.sleep(3)


