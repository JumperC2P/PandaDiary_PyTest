import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
from Admin_Register import Admin_Register
import platform

WEB_URL = "http://localhost:3000/"


class Admin_Register_Test(unittest.TestCase):

    def setUp(self):
        self.admin = {
            'email': 'zbhu7e9u@gmail.com',
            'password': '12345678'
        }
        self.new_user = {
            'username': 'TestingAdmin',
            'email': 'testing_admin@gmail.com',
            'password': '12345678',
            'confirmed_password': '12345678'
        }
        self.new_user1 = {
            'username': 'TestinggA',
            'email': 'testing1_a@gmail.com',
            'password': '12345678',
            'confirmed_password': '12345678'
        }
        self.new_user2 = {
            'username': 'TestinggGA',
            'email': 'testing2_a@gmail.com',
            'password': '12345678',
            'confirmed_password': '12345678'
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

    def test_register_admin(self):
        expected = "Add admin successful."
        is_first = True
        is_second = True
        for k in self.drivers:
            if is_first and is_second:
                user = self.new_user
                is_first = False
            elif is_second:
                user = self.new_user1
                is_second = False
            else: 
                user = self.new_user2

            result = Admin_Register().start(self.drivers[k], self.admin, user)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
