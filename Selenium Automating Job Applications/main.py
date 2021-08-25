from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PHONE = "YOUR PHONE NUMBER"
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"


chrome_driver = "chromediver path"

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.linkedin.com/jobs/search/?geoId=103588929&keywords=python%20backend&location=Seoul%2C%20South%20Korea")




login = driver.find_element_by_link_text("Войти")
login.click()

email_field = driver.find_element_by_id("username")
email_field.send_keys(EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(5)


all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for jobs in all_jobs:
    print("called")
    jobs.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone_field = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone_field.text == "":
            phone_field.send_keys(PHONE)

        elif phone_field.text != "":
            phone_field.clear()

        # Submit the application
        submit_button = driver.find_element_by_css_selector("footer button")


        #if Two or more step application form , cancel the form with cancel button
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)

            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()


    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()