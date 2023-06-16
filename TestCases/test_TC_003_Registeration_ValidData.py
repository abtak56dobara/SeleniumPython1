import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegisterationPage

def dataGenerator():
    li = [ ['uname1','pass1'] ,['uname2','pass2'] , ['uname3','pass3'] ]  # data in list
    return li

@pytest.mark.parametrize('data',dataGenerator())
def test_ValidateRegistration(data):
    driver=InitiateDriver.startBrowser()
    register=RegisterationPage.Registerationclass(driver)
    register.enter_Username(data[0])
    register.enter_email(data[1])
    time.sleep(2)
    driver.close()