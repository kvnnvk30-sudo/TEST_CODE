from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class   MAIN(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def search_input(self):
        search_field = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "search"))
        )

        # Clear it first just in case there's placeholder text
        search_field.clear()
        search_field.send_keys("Selenium (software)" + Keys.RETURN)
