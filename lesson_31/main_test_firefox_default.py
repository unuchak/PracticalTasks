import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class TestTestrail(unittest.TestCase):

    def test_required_fields(self):
        options = Options()
        options.binary_location = "/usr/bin/firefox"
        driver = webdriver.Firefox(options=options, service=Service())
        driver.implicitly_wait(30)
        driver.get("https://www.google.com/")
        driver.maximize_window()
        driver.find_element(
            By.NAME, "q").send_keys("selenium")
        driver.find_element(
            By.NAME, "q").send_keys(Keys.ENTER)
        driver.find_element(
            By.CSS_SELECTOR,
            "#rso > div:nth-child(1) > div > div > div > div > div > div > div > a > div > div > div > cite"
        ).click()
        text2 = driver.title

        self.assertEqual(text2, "Selenium")
        driver.quit()
