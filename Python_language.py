from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Python_class(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def Python(self):
        self.wait.until(EC.url_contains("/Python_(programming_language)"))
        assert "Python" in self.driver.page_source