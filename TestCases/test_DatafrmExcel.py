import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegisterationPage
import openpyxl
from DataGenerator import DataGen

#we can call module method by its name
@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver=InitiateDriver.startBrowser()
    register=RegisterationPage.Registerationclass(driver)
    register.enter_Username(data[0])
    register.enter_email(data[1])
    time.sleep(2)
    driver.close()