from selenium.webdriver.common.by import By
from  Library import ConfigReader

class Registerationclass:
    def __init__(self,obj):
        global driver
        driver=obj

    def enter_Username(self,name):
        driver.find_element(By.NAME, ConfigReader.fetchElementLocators("Registration", "username_name")).send_keys(name)

    def enter_password(self,pswd):
        driver.find_element(By.NAME, ConfigReader.fetchElementLocators("Registration", "password_name")).send_keys(pswd )

    def enter_email(self,email):
        driver.find_element(By.NAME, ConfigReader.fetchElementLocators("Registration", "email_name")).send_keys(email )

