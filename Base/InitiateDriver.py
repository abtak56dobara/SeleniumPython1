from selenium import webdriver
from Library import ConfigReader


def startBrowser():
    global driver

    if(ConfigReader.readConfigData('Details','Browser'))=="chrome":
        driver = webdriver.Chrome()
    elif(ConfigReader.readConfigData('Details','Browser'))=="firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()
