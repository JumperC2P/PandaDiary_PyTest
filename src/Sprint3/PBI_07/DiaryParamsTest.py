import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
from DiaryParams import DiaryParams
import platform

WEB_URL = "http://localhost:3000/"


class DiaryParamsTest(unittest.TestCase):

    def setUp(self):
        self.admin = {
            'email': 'zbhu7e9u@gmail.com',
            'password': '12345678'
        }

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
            # self.firefox_driver = webdriver.Firefox(executable_path=((str)(firefox_driver_path)))
            # self.safari_driver = webdriver.Safari()

        self.drivers = {}

        if platform.system() == 'Windows':
            self.drivers['Edge'] = self.edge_driver
        else:
            self.drivers['Chrome'] = self.chrome_driver
            # self.drivers['Firefox'] = self.firefox_driver
            # self.drivers['Safari'] = self.safari_driver

        for browser in self.drivers:
            self.drivers[browser].implicitly_wait(10)
            self.drivers[browser].get(WEB_URL)
            self.drivers[browser].set_window_size(1440, 1080)

    def tearDown(self):
        for k in self.drivers:
            self.drivers[k].close()

    def test_add_params(self):
        expected = 3
        for k in self.drivers:
            result = DiaryParams().start_add(self.drivers[k], self.admin, 'Test')
            self.assertEqual(expected, result)

    def test_delete_params(self):
        expected = 3
        for k in self.drivers:
            result = DiaryParams().start_delete(self.drivers[k], self.admin)
            self.assertEqual(expected, result)

    def test_recover_params(self):
        expected = 3
        for k in self.drivers:
            result = DiaryParams().start_recover(self.drivers[k], self.admin)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
