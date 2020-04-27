import unittest;
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
        
        chrome_options = Options()
        self.chrome_driver = webdriver.Chrome(executable_path=((str)(pathlib.Path().absolute()))+'/chromedriver', chrome_options=chrome_options)
        self.chrome_driver.implicitly_wait(10)
        self.chrome_driver.get(WEB_URL)

        self.firefox_driver = webdriver.Firefox(executable_path=((str)(pathlib.Path().absolute()))+'/geckodriver')
        self.firefox_driver.implicitly_wait(10)
        self.firefox_driver.get(WEB_URL)

        self.drivers = {
            'Chrome': self.chrome_driver,
            'Firefox': self.firefox_driver
        }

        if (platform.system() == 'Windows'):
            self.ie_driver = webdriver.Firefox(executable_path=((str)(pathlib.Path().absolute()))+'/IEDriverServer.exe')
            self.ie_driver.implicitly_wait(10)
            self.ie_driver.get(WEB_URL)
            self.drivers['IE'] = self.ie_driver


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
        for k in self.drivers:
            if is_first:
                user = self.user
                is_first = False
            else:
                user = self.user1

            result = self.register_success(self.drivers[k], user)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()