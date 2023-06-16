from selenium import webdriver
import time
import  pytest
from selenium.webdriver.common.by import By

@pytest.fixture()
def environment_setup():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://thetestingworld.com/testings/index.php?message=4")
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registeration(environment_setup):
    driver.find_element(By.XPATH,"//*[text()='Login']").click()
    driver.find_element(By.XPATH,"//*[@name='_txtUserName']").send_keys("test123!@#")
    driver.find_element(By.XPATH,"//*[@name='_txtPassword']").send_keys("test")
    driver.find_element(By.XPATH,"//*[@value='Login']").click()
    driver.find_element(By.XPATH,"//li//*[contains(text(),' My Account')]").click()
    driver.find_element(By.XPATH, "(//a[contains(text(),'Update')])[1]").click()
    time.sleep(2)
    all_windows=driver.window_handles
    mainWin=""
    for win in all_windows:
        driver.switch_to.window(win)
        print(driver.current_url)
        if(driver.current_url=='https://thetestingworld.com/testings/manage_customer.php'):
            driver.find_element(By.XPATH,"//button[@id='downloadButton']").click()
            time.sleep(9)
        else:
            mainWin=win

    driver.switch_to.window(mainWin)
    print(driver.current_url)

