import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_vwologin():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    chrome_options.add_extension("C:/Users/manib/Downloads/AdBlock.crx")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://youtube.com")
    time.sleep(3)
