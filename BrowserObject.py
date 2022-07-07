from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from AppSettings import get_application_settings
from PageObjects.Permit.PermitLandingPage import PermitLanding
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class Browser:
    driver: WebDriver
    config = get_application_settings()

    def __init__(self):
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def navigate_to_permits(self) -> PermitLanding:
        self.driver.get(self.config.permit.url)
        if self.config.permit.welcome_page:
            return PermitLanding(self.driver)

    def close(self) -> None:
        self.driver.close()
