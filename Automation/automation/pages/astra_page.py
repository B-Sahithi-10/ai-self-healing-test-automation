import os
from selenium.webdriver.common.by import By

class AstraPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "file://" + os.path.abspath("automation/mock_ui.html")

    def open(self):
        self.driver.get(self.url)

    def analyze_code(self, code):
        self.driver.find_element(By.ID, "codeInput").send_keys(code)
        self.driver.find_element(By.ID, "analyzeBtn").click()

    def get_output(self):
        return self.driver.find_element(By.ID, "output").text
