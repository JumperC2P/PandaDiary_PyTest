import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
from Review import Review
import platform

WEB_URL = "http://localhost:3000/"


class ReviewTest(unittest.TestCase):

    def setUp(self):
        self.user = {
            'email': 'test@gmail.com',
            'password': '12345678',
        }
        self.order1 = '2020050611'
        self.order2 = '2020050612'
        self.order3 = '2020050613'


        chrome_options = Options()

        if platform.system() == 'Windows':
            self.edge_driver = webdriver.Edge()
            self.edge_driver.implicitly_wait(10)
            self.edge_driver.get(WEB_URL)
        else:
            driver_path = (str(pathlib.Path().absolute())) + '/linux_driver'
            chrome_driver_path = driver_path + '/chromedriver'
            firefox_driver_path = driver_path + '/geckodriver'
            self.chrome_driver = webdriver.Chrome(executable_path=((str)(chrome_driver_path)),
                                                  chrome_options=chrome_options)
            self.firefox_driver = webdriver.Firefox(executable_path=((str)(firefox_driver_path)))
            self.safari_driver = webdriver.Safari()

        self.drivers = {}

        if platform.system() == 'Windows':
            self.drivers['Edge'] = self.edge_driver
        else:
            self.drivers['Chrome'] = self.chrome_driver
            self.drivers['Firefox'] = self.firefox_driver
            self.drivers['Safari'] = self.safari_driver

        for browser in self.drivers:
            self.drivers[browser].implicitly_wait(10)
            self.drivers[browser].get(WEB_URL)
            self.drivers[browser].set_window_size(1440, 1080)

    def tearDown(self):
        for k in self.drivers:
            self.drivers[k].close()

    def test_add_review(self):
        expected = "Thank your for giving a review."
        is_first = True
        is_second = True
        count = 3
        for k in self.drivers:
            if is_first and is_second:
                order_id = self.order1
                is_first = False
            elif is_second:
                order_id = self.order2
                is_second = False
            else: 
                order_id = self.order3

            result = Review().start(self.drivers[k], self.user, order_id, str(count), "Unit testing")
            self.assertEqual(expected, result)
            count = count + 1


if __name__ == '__main__':
    unittest.main()
