# Selenium Mini Project #3
#
# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password
# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end
#
# augtest_040823@idrive.com
# 123456

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.positive
@allure.title("iDrive360 Trial Page - test_mini_project_3")
@allure.description("Verify that Trial is finished and current URL also")
def test_mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    # <input _ngcontent-jqi-c4="" autofocus="" class="id-form-ctrl ng-pristine ng-valid ng-touched" id="username"
    # name="username" type="email" fdprocessedid="yj06rt">
    email_webelement = driver.find_element(By.ID, "username")
    email_webelement.send_keys("augtest_040823@idrive.com")

    # <input _ngcontent-jqi-c4="" class="id-form-ctrl ng-pristine ng-valid ng-touched" id="password" maxlength="20"
    # name="password" tabindex="0" type="password" fdprocessedid="f1b3gh">
    password_webelement = driver.find_element(By.ID, "password")
    password_webelement.send_keys("123456")

    # <button _ngcontent-jqi-c4="" class="id-btn id-info-btn-frm" id="frm-btn" type="submit"
    # fdprocessedid="01nzhe">Sign in</button>
    submit_webelement = driver.find_element(By.ID, "frm-btn")
    submit_webelement.click()
    time.sleep(20)
    #<span _ngcontent-vcu-c3="">Your free trial has expired</span>
    # trial_element = driver.find_element(By.XPATH, "//span[text()='Your free trial has expired']")
    trial_element = driver.find_element(By.XPATH, "//span[text()='Your free trial has expired']")
    # assert trial_element.text == "Your free trial has expired"
    # assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    assert (driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true") and (
            trial_element.text == "Your free trial has expired")

    allure.attach(driver.get_screenshot_as_png(), name='Mini_Project_3', attachment_type=AttachmentType.PNG)
    driver.close()
