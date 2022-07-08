from __future__ import annotations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.Permit.EkashuPage import Ekashu

class PermitCheckout:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def agree_to_terms(self) -> PermitCheckout:
        self.driver.find_element(By.ID, "termsCheckBox").click()
        return self

    def select_make_a_payment(self) -> Ekashu:
        WebDriverWait(self.driver, 60)\
            .until(
                EC.presence_of_element_located(
                    (By.XPATH, '//span[text()="Make a payment"]')
                    )
                ).click()
        return Ekashu(self.driver)