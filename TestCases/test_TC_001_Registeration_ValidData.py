import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegisterationPage


def test_ValidateRegistration():
    driver=InitiateDriver.startBrowser()
    register=RegisterationPage.Registerationclass(driver)
    register.enter_Username("hello")
    register.enter_email("asd@mcd.com")
    time.sleep(2)
    driver.close()