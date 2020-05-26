import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
from ReportDownload import ReportDownload
import platform
import os
import time

WEB_URL = "http://localhost:3000/"


class ReportDownloadTest(unittest.TestCase):

    def setUp(self):
        self.admin = {
            'email': 'zbhu7e9u@gmail.com',
            'password': '12345678'
        }

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        chrome_options.add_experimental_option("prefs", {
                "download.default_directory": (str(pathlib.Path().absolute())) + "/",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
        })
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", (str(pathlib.Path().absolute())) + "/")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")

        capabilities = webdriver.DesiredCapabilities().SAFARI.copy()
        capabilities['safari.options.dataDir'] = (str(pathlib.Path().absolute())) + "/"

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
            self.firefox_driver = webdriver.Firefox(executable_path=((str)(firefox_driver_path)),firefox_profile=profile)
            self.safari_driver = webdriver.Safari(desired_capabilities=capabilities)

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

    def test_download_report_weekly(self):
        expected = "report-weekly.csv"
        for k in self.drivers:
            ReportDownload().start(self.drivers[k], self.admin, '0')

            f= open((str(pathlib.Path().absolute())) + "/report-weekly.csv")
            file_name = os.path.basename(f.name)
            self.assertEqual(expected, file_name)
            time.sleep(5)
            f.close()

    def test_download_report_monthly(self):
        expected = "report-monthly.csv"
        for k in self.drivers:
            ReportDownload().start(self.drivers[k], self.admin, '1')

            f= open((str(pathlib.Path().absolute())) + "/report-monthly.csv")
            file_name = os.path.basename(f.name)
            self.assertEqual(expected, file_name)
            f.close()


if __name__ == '__main__':
    unittest.main()
