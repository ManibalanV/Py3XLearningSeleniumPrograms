# Selenium Project#4 - Mini Project
#
# open the url - https://katalon-demo-cura.herokuapp.com/
# click on the make appointment button
# verify that url changes - assert
# time.sleep(3)
# enter the username, password
# next page verify the current url
# make appointment text on the web page.
# Upload them GitHub.com

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.positive
@allure.title("Katalon appointment - test_mini_project_4")
@allure.description("Make appointment and check the current URL")
def test_mini_project_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #<a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    make_appointment_webelement = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_webelement.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)
    # <input type="text" class="form-control" id="txt-username" name="username" placeholder="Username" value=""
    # autocomplete="off" fdprocessedid="r5il7vd">
    username_webelement = driver.find_element(By.ID, "txt-username")
    username_webelement.send_keys("John Doe")
    # <input type="password" class="form-control" id="txt-password" name="password" placeholder="Password" value=""
    # autocomplete="off" fdprocessedid="h2ri5g">
    password_webelement = driver.find_element(By.ID, "txt-password")
    password_webelement.send_keys("ThisIsNotAPassword")
    #<button id="btn-login" type="submit" class="btn btn-default" fdprocessedid="ehcjud">Login</button>
    login_webelement = driver.find_element(By.ID, "btn-login")
    login_webelement.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    allure.attach(driver.get_screenshot_as_png(), name='Mini_Project_4', attachment_type=AttachmentType.PNG)
    driver.close()
