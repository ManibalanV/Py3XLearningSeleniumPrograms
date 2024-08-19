from selenium import webdriver


def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    # Wait for potential redirection if needed
    # current_url = driver.current_url
    # assert current_url.startswith("https://www.google.com/")
    assert driver.current_url == "https://www.google.com/"
    driver.quit()  # It's a good practice to close the driver after the test
