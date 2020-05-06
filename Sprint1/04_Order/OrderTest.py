import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path
import platform
from Order import Order
from datetime import date

# WEB_URL = "https://pandadiary-275703.ts.r.appspot.com/login"
WEB_URL = "http://localhost:3000/payment"

class DeliverySelectionTest(unittest.TestCase):



    def setUp(self):

        self.info = {
            'payment_option': '2',
            'card_number': '1234567812345678',
            'expired_date_m': '04',
            'expired_date_m': '2022',
            'security_code': '123',
            'delivery_option': '2',
            'username': 'Testing',
            'phone': '0123456789',
            'address': '777 Swanston Street',
        }
        
        chrome_options = Options()
        
        if (platform.system() == 'Windows'):
            self.edge_driver = webdriver.Edge()
            self.edge_driver.implicitly_wait(10)
            self.edge_driver.get(WEB_URL)
        else:
            driver_path = ((str)(os.path.abspath(os.curdir))) + '/linux_driver'
            chrome_driver_path = driver_path + '/chromedriver'
            firefox_driver_path = driver_path + '/geckodriver'
            self.chrome_driver = webdriver.Chrome(executable_path=((str)(chrome_driver_path)), chrome_options=chrome_options)
            self.firefox_driver = webdriver.Firefox(executable_path=((str)(firefox_driver_path)))
            self.safari_driver = webdriver.Safari()


        self.drivers = {}

        if (platform.system() == 'Windows'):
            self.drivers['Edge'] = self.edge_driver
        else:
            self.drivers['Chrome'] = self.chrome_driver
            self.drivers['Firefox'] = self.firefox_driver
            self.drivers['Safari'] = self.safari_driver

        for browser in self.drivers:
            self.drivers[browser].implicitly_wait(10)
            self.drivers[browser].get(WEB_URL)
            self.drivers[browser].set_window_size(1440,1080)

    def tearDown(self):
        for k in self.drivers:
            self.drivers[k].close()

    def send_order(self, driver):
        return Order().start(driver, self.info)

    def test_send_order(self):
        expected = date.today().strftime("%Y%m%d")
        for k in self.drivers:
            result = self.send_order(self.drivers[k])
            self.assertEqual(expected, result[21:29])


if __name__ == '__main__':
    unittest.main()
