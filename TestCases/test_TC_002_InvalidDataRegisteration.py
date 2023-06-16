import time
from selenium.webdriver.common.by import By
from Library import ConfigReader

from Base import InitiateDriver

def test_registeration_invalid_data():
    driver=InitiateDriver.startBrowser()

    driver.find_element(By.NAME, ConfigReader.fetchElementLocators("Registration","password_name")).send_keys("hello")
    time.sleep(2)
    driver.close()