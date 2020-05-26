import time
import json


class ReportDownload:

    def start(self, driver, user, option):
        try:
            sign_in_link = driver.find_element_by_xpath('//a[@href="/login"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            sign_in_link = driver.find_element_by_xpath('//a[@href="/login"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        sign_in_link.click()

        driver.find_element_by_name('emailLogin').send_keys(user['email'])
        driver.find_element_by_name('passwordLogin').send_keys(user['password'])
        driver.find_element_by_css_selector("button[class='ui button'][type='button']").click()

        time.sleep(3)

        # go to diary management
        try:
            report_link = driver.find_element_by_xpath('//a[@href="/admin/report"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            report_link = driver.find_element_by_xpath('//a[@href="/admin/report"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        report_link.click()


        driver.find_element_by_css_selector("option[value='"+option+"']").click()
        driver.find_element_by_css_selector("button[type='button'][class='btn btn-success']").click()
        time.sleep(3)