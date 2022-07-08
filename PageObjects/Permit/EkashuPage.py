from __future__ import annotations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from AppSettings import get_application_settings
from PageObjects.Permit.PermitCompletedPage import PermitCompleted

class Ekashu: 
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        self.config = get_application_settings()
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'ekashu_section_title_card'), 'Credit or Debit Card'))

    def fill_in_card_details(self) -> Ekashu:
        self.driver.find_element(By.ID, 'ekashu_card_number').send_keys(self.config.test_card.card_number)
        self.driver.find_element(By.ID, 'ekashu_input_expires_end_month').send_keys(self.config.test_card.expiry_month)
        self.driver.find_element(By.ID, 'ekashu_input_expires_end_year').send_keys(self.config.test_card.expiry_year)
        self.driver.find_element(By.ID, 'ekashu_verification_value').send_keys(self.config.test_card.security_code)
        return self

    def complete_payment(self) -> PermitCompleted:
        self.driver.find_element(By.ID, 'ekashu_submit_continue_button').click()
        return PermitCompleted(self.driver)



        