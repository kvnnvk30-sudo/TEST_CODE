from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class W(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(" https://www.wikipedia.org")


    def english_leng(self):
        english = self.wait.until(EC.element_to_be_clickable((By.ID, "js-link-box-en")))
        english.click()


