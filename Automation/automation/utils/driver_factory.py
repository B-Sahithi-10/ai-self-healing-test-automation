from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")

    # Selenium Manager (cross-platform, no driver download code)
    driver = webdriver.Chrome(options=options)

    return driver
