from __future__ import annotations
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .PermitCheckoutPage import PermitCheckout

class PermitSchedule:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".TitleText"), "Select your travel dates"))

    def add_a_day(self) -> PermitSchedule:
        self.driver.find_element(By.CSS_SELECTOR, '.c-split-content__form-group__button').click()
        return self

    def select_continue(self) -> PermitCheckout: 
        WebDriverWait(self.driver, 60)\
            .until(
                EC.presence_of_element_located(
                    (By.XPATH, '//button[text()="Continue"]')
                    )
                ).click()
        return PermitCheckout(self.driver)