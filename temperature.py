from time import sleep
from selenium import webdriver
import random
import schedule
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox(executable_path='/Users/shawn/Downloads/geckodriver')
browser.implicitly_wait(5)
browser.get('http://go.gov.sg/mindeftemp')
sleep(1)
proceed = browser.find_element_by_xpath("/html/body/main/div/button/div/p")
proceed.click()
sleep(1)

def submittemp():
    id = browser.find_element_by_id("5e46432e351f7400111de7f9")
    sleep(1)
    id.click()
    sleep(1)
    id.send_keys('XXXXXXXX')

    no = browser.find_element_by_xpath("/html/body/section/section/div/submit-form-directive/div[1]/div[1]/div/form/div[2]/field-directive/div/yes-no-field-component/div/div[2]/div/label[1]")
    sleep(1)
    no.click()

    temperature = browser.find_element_by_id("5e4537cad13e110011aaa2a5")
    sleep(1)
    temperature.click()
    sleep(1)
    num = round(random.uniform(36.1, 37.2), 1)
    temperature.send_keys(str(num))

    submit = browser.find_element_by_xpath("/html/body/section/section/div/div[1]/div/div/div/div/button")
    sleep(1)
    submit.click()

    print('Temperature submitted')

schedule.every().day.at("07:00").do(submittemp)
schedule.every().day.at("12:00").do(submittemp)

while True:
    schedule.run_pending()
    time.sleep(1)





