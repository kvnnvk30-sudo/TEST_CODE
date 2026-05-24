from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Main_Page import MAIN
from Python_language import Python_class
from Selenium_software import software
from Wiki import W


def test_www(driver):
    WWW = W(driver)
    Pege=MAIN(driver)
    Selen = software(driver)
    Py = Python_class(driver)
    WWW.open()
    WWW.english_leng()
    Pege.search_input()
    Selen.Selenium()
    Selen.Selenium_paragraph()
    Selen.python_click()
    Py.Python()

