import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
from Register import Register
import platform

WEB_URL = "https://pandadiary.ts.r.appspot.com"

class RegisterTest(unittest.TestCase):


    def setUp(self):
        self.user = {
            'username': 'Testing',
            'email': 'testing@gmail.com',
            'password': '12345678',
            'confirmed_password': '12345678'
        }
        self.user1 = {
            'username': 'Testingg',
            'email': 'testing1@gmail.com',
            'password': '12345678',
            'confirmed_password': '12345678'
        }
        self.user2 = {
            'username': 'TestinggG',
            'email': 'testing2@gmail.com',
            'password': '12345678',
            'confirmed_password': '12345678'
        }
        
        chrome_options = Options()
        
        if (platform.system() == 'Windows'):
            self.edge_driver = webdriver.Edge()
            self.edge_driver.implicitly_wait(10)
            self.edge_driver.get(WEB_URL)
        else:
            driver_path = ((str)(pathlib.Path().absolute())) + '/linux_driver'
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
        return super().tearDown()

    def register_no_capital_name(self, driver):
        self.user['username'] = 'testing'
        return Register().start(driver, self.user, True)

    def register_wrong_email(self, driver):
        self.user['email'] = 'testinggmail.com'
        return Register().start(driver, self.user, True)

    def register_wrong_password(self, driver):
        self.user['confirmed_password'] = '1234583930'
        return Register().start(driver, self.user, True)

    def register_not_checked(self, driver):
        return Register().start(driver, self.user, False)

    def register_success(self, driver, user):
        return Register().start(driver, user, True)

    def test_register_no_capital_name(self):
        print(platform.system())
        expected = "Please make sure details you've entered are correct!"
        for k in self.drivers:
            result = self.register_no_capital_name(self.drivers[k])
            self.assertEqual(expected, result)

    def test_register_wrong_email(self):
        expected = "Please make sure details you've entered are correct!"
        for k in self.drivers:
            result = self.register_wrong_email(self.drivers[k])
            self.assertEqual(expected, result)

    def test_register_wrong_password(self):
        expected = "Please make sure details you've entered are correct!"
        for k in self.drivers:
            result = self.register_wrong_password(self.drivers[k])
            self.assertEqual(expected, result)

    def test_register_not_checked(self):
        expected = "Please make sure you've checked the box!"
        for k in self.drivers:
            result = self.register_not_checked(self.drivers[k])
            self.assertEqual(expected, result)

    def test_register_success(self):
        expected = "Registration successful."
        is_first = True
        is_second = True
        for k in self.drivers:
            if is_first and is_second:
                user = self.user
                is_first = False
            elif is_second:
                user = self.user1
                is_second = False
            else: 
                user = self.user2

            result = self.register_success(self.drivers[k], user)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()