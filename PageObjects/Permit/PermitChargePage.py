from __future__ import annotations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class PermitCharge:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def get_charge(self) -> float:
        text_list = self.driver.find_elements(By.TAG_NAME, "p")
        for i in text_list:
            if i.text.__contains__("Standard charge per day"):
                pre_text, value = i.text.split("£")
                return float(value)
        raise Exception("Unable to find charge for permit on charge page")
