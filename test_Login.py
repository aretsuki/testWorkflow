from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

username = "alexkoval"
email = "a.koval508@gmail.com"
password = "login123"
url = "https://juno.one"


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
            driver = self.driver
            try:
                driver.get(url)
                driver.maximize_window()
            except Exception as ex:
                print(ex)
            else:
                time.sleep(10)
                driver.find_element(By.CSS_SELECTOR, ".pointer[data-v-3cdce82b]").click()
    def tearDown(self):
            self.driver.quit()

if __name__ == "main":
    unittest.main()