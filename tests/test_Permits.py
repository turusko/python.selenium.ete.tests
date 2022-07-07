import unittest
from BrowserObject import Browser


class Permits(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = Browser()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()

    def test_vehicle_can_be_looked_up(self) -> None:
        permits = self.browser.navigate_to_permits()
        self.assertTrue(permits.is_page_tile_displayed(), "Permits webpage did not start up")
        data = permits.click_next().lookup_vrm("t2omf")
        self.assertTrue(data[0].text.__contains__('T2OMF'))
        self.assertTrue(data[1].text.__contains__('JAGUAR'))
        self.assertTrue(data[2].text.__contains__('BLACK'))

    def test_vehicle_can_be_looked_up_two(self) -> None:
        permits = self.browser.navigate_to_permits()
        self.assertTrue(permits.is_page_tile_displayed(), "Permits webpage did not start up")
        data = permits.click_next().lookup_vrm("t2omf")
        self.assertTrue(data[0].text.__contains__('T2OMF'))
        self.assertTrue(data[1].text.__contains__('JAGUAR'))
        self.assertTrue(data[2].text.__contains__('BLACK'))



