from selenium.webdriver.remote.webdriver import WebDriver

class PermitSchedule:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

        