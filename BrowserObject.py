from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from AppSettings import get_application_settings
from pageObjects import PermitLanding
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options


class Browser:
    driver: WebDriver
    config = get_application_settings()

    def __init__(self):
        options = Options()
        options.headless = self.config.headless
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

    def navigate_to_permits(self) -> PermitLanding:
        self.driver.get(self.config.permit.url)
        if self.config.permit.welcome_page:
            return PermitLanding(self.driver)

    def close(self) -> None:
        self.driver.close()
