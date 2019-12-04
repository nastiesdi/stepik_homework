from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome(executable_path='C:\chromedriver/chromedriver.exe')

try:
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[placeholder ="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.third')
    input3.send_keys('fff@llll')
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(30)
    browser.quit()

# import unittest
#
#
# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()