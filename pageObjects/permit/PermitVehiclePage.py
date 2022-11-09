from __future__ import annotations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from .PermitChargePage import PermitCharge


class PermitVehicle:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def lookup_vrm(self, vrm: str, valid: bool = True) -> List[WebElement]:
        self.__enter_vrm(vrm)
        if valid:
            self.__click_find_vehicle()
            self.__wait_for_progress_button()
            return self.driver.find_elements(By.CSS_SELECTOR, ".VehcileDetailine")
        else:
            return []

    def confirm_vehicle(self) -> PermitCharge:
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue"]')))
        element.click()
        return PermitCharge(self.driver)

    def get_error_message(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".k-form-error.k-invalid-msg").text    

    def no_search_again(self) -> None:
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="No"]'))).click()
        self.driver.find_element(By.XPATH, '//button[text()="Continue"]').click()

    def clear_vrm_input_box(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "#vrmInput").clear()

    def is_progress_button_enabled(self) -> bool:
        return self.driver.find_element(By.XPATH, '//button[text()="Continue"]').is_enabled()

    def __wait_for_progress_button(self) -> None:
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Continue"]')))

    def __enter_vrm(self, vrm: str) -> None:
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#vrmInput"))).send_keys(vrm)

    def __click_find_vehicle(self) -> None:
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'button'))).click()
