import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestTestrail(unittest.TestCase):

    def test_required_fields(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(30)
        driver.get("https://www.testrail.com/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Platform").click()
        driver.find_element(By.LINK_TEXT, "Enterprise").click()
        driver.find_element(By.CSS_SELECTOR, ".breakdance-menu-item-22-112 > .breakdance-menu-link").click()
        driver.find_element(By.CSS_SELECTOR, ".button-atom--secondary").click()
        driver.find_element(By.ID, "first_name").click()
        driver.find_element(By.ID, "first_name").send_keys("Marina")
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        text1 = driver.find_element(By.CSS_SELECTOR, ".form-error:nth-child(1)").text
        text2 = driver.find_element(By.CSS_SELECTOR, ".form-error:nth-child(2)").text

        self.assertEqual(text1, "Last Name field is required.")
        self.assertEqual(text2, "Email Address field is required.")
        driver.quit()
