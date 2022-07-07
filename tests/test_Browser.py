import imp
import unittest
from time import sleep
from BrowserObject import Browser


class BrowserTests(unittest.TestCase):
    def test_check_browser(self):
        x = Browser()
        x.navigate_to_permits()

        
if __name__ == '__main__':
	unittest.main()