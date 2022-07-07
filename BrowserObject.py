from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
from AppSettings import get_application_settings

class Browser:
    driver: WebDriver
    config = get_application_settings()

    def __init__(self):
        self.driver = webdriver.Edge(executable_path="c:/drivers/msedgedriver.exe")
        self.driver.maximize_window()
    
    def navigate_to_permits(self):
        self.driver.get(self.config.permit)

        