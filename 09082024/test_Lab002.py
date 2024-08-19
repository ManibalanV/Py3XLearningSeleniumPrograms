from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()
    print(driver.session_id) # 742d32512db378eb3a3b1146b8183a7d
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(3)

