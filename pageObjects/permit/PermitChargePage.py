from __future__ import annotations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .PermitSchedulePage import PermitSchedule

class PermitCharge:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def get_charge(self) -> float:
        text_list = self.driver.find_elements(By.TAG_NAME, "p")
        for i in text_list:
            if i.text.__contains__("Standard charge per day"):
                output = i.text.split("£")
                return float(output[1])
        raise KeyError("Unable to find charge for permit on charge page")
    
    def click_select_travel_dates(self) -> PermitSchedule:
        WebDriverWait(self.driver, 60)\
            .until(EC\
                .presence_of_element_located(
                    (By.XPATH, '//button[text()="Select your travel dates"]')
                    )
                ).click()
        return PermitSchedule(self.driver)
