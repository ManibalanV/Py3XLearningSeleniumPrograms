#Mini project #2:

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure


@pytest.mark.positive
@allure.title("VWO Invalid Login Page - test_mini_project_2")
@allure.description("Verify that with Invalid Email, password. Error message came")
def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"
    # <input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi"
    # fdprocessedid="964mqd">
    email_webelement = driver.find_element(By.ID, "login-username")
    email_webelement.send_keys("admin@admin.com")
    # <input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe"
    # fdprocessedid="80prz">
    password_webelement = driver.find_element(By.ID, "login-password")
    password_webelement.send_keys("admin@123")
    # #<button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)" data-qa="sibequkica" fdprocessedid="jeu4w"> <span class="icon loader hidden"
    # data-qa="zuyezasugu"></span> <span data-qa="ezazsuguuy">Sign in</span> </button>on>
    submit_webelement = driver.find_element(By.ID, "js-login-btn")
    submit_webelement.click()
    time.sleep(5)
    # <div class="notification-box-description" id="js-notification-box-msg" data-qa="rixawilomi">Your email,
    # password, IP address or location did not match</div>
    error_msg_webelement = driver.find_element(By.ID, "js-notification-box-msg")

    assert error_msg_webelement.text == "Your email, password, IP address or location did not match"

    time.sleep(5)

    driver.quit()
