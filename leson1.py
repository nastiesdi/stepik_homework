import time
import math
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome(executable_path='C:\chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), str(100)))
but = browser.find_element_by_id("book")
but.click()
num = browser.find_element_by_id('input_value').text
res = calc(int(num))
field = browser.find_element_by_id('answer')
field.send_keys(res)
but_sub = browser.find_element_by_id("solve")
but_sub.click()









# time.sleep(1)


