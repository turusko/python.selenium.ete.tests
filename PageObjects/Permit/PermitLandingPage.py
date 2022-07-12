from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Permit.PermitVehiclePage import PermitVehicle


class PermitLanding:
    driver: WebDriver

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".Title"), "Zero Emission Zone (ZEZ)"))

    def is_page_tile_displayed(self) -> bool:
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Title")))
        return self.driver.find_element(By.CSS_SELECTOR, ".Title").text == "Zero Emission Zone (ZEZ)"

    def click_next(self) -> PermitVehicle:
        self.driver.find_element(By.CSS_SELECTOR, ".BoxedText").click()
        return PermitVehicle(self.driver)