#Payment Confirmed
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PermitCompleted: 
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.TitleText'), 'Payment Confirmed'))