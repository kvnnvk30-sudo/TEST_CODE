from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class software(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def Selenium(self):
        Selenium = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "mw-page-title-main")))
        text = "Selenium (software)"
        assert Selenium.text == text


    def Selenium_paragraph(self):
        first_paragraph = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class, 'mw-parser-output')]/p[not(@class)]")
        ))
        assert "browser automation" in first_paragraph.text


    def python_click(self):
        python = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/wiki/Python_(programming_language)']")))
        python.click()