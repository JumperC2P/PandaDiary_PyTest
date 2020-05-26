import time
import json


class UpdateUser:

    def start(self, driver, user, id):
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
            user_link = driver.find_element_by_xpath('//a[@href="/admin/user"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            user_link = driver.find_element_by_xpath('//a[@href="/admin/user"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        user_link.click()

        driver.find_element_by_id(id+'-detail-btn').click()
        time.sleep(2)
        driver.find_element_by_id('user_suburb').send_keys(driver.find_element_by_id('user_suburb').text+' Auto Testing')
        driver.find_element_by_css_selector("button[type='button'][class='menu-button btn btn-success']").click()
        time.sleep(2)
        result = driver.find_element_by_id('swal2-title').text

        return result