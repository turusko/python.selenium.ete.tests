# import unittest
# from BrowserObject import Browser
# from time import sleep
# from AppSettings import get_application_settings


# class Permits(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.browser = Browser()

#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.browser.close()

#     def test_vehicle_can_be_looked_up(self) -> None:
#         config = get_application_settings()
#         permits = self.browser.navigate_to_permits()
#         self.assertTrue(permits.is_page_tile_displayed(), "Permits webpage did not start up")
#         vehicle_lookup_page = permits.click_next()
#         data = vehicle_lookup_page.lookup_vrm(config.vehicle_details.vrm)
#         self.assertTrue(data[0].text.__contains__(config.vehicle_details.vrm))
#         self.assertTrue(data[1].text.__contains__(config.vehicle_details.make))
#         self.assertTrue(data[2].text.__contains__(config.vehicle_details.colour))
#         charge_page = vehicle_lookup_page.confirm_vehicle()
#         self.assertEqual(charge_page.get_charge(), 10)
#         schedule_page = charge_page.click_select_travel_dates()
#         checkout_page = schedule_page.add_a_day().select_continue()
#         checkout_page.agree_to_terms()\
#             .select_make_a_payment()\
#             .fill_in_card_details()\
#             .complete_payment()
            

       
        






