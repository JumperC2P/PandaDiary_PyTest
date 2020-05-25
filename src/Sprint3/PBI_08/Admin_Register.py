import time
import json


class Admin_Register:

    def start(self, driver, admin, user):
        try:
            sign_in_link = driver.find_element_by_xpath('//a[@href="/login"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            sign_in_link = driver.find_element_by_xpath('//a[@href="/login"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        sign_in_link.click()

        driver.find_element_by_name('emailLogin').send_keys(admin['email'])
        driver.find_element_by_name('passwordLogin').send_keys(admin['password'])
        driver.find_element_by_css_selector("button[class='ui button'][type='button']").click()

        time.sleep(3)

         # go to diary management
        try:
            user_link = driver.find_element_by_xpath('//a[@href="/admin/user"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            user_link = driver.find_element_by_xpath('//a[@href="/admin/diuserary"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        user_link.click()

        driver.find_element_by_css_selector("button[class='menu-button btn btn-light'][type='button']").click()

        driver.find_element_by_name('username').send_keys(user['username'])
        driver.find_element_by_name('email').send_keys(user['email'])
        driver.find_element_by_name('password').send_keys(user['password'])
        driver.find_element_by_name('confirmPassword').send_keys(user['confirmed_password'])
        driver.find_element_by_name('terms').click()
        driver.find_element_by_css_selector("button[type='submit'][class='ui button']").click()
        time.sleep(2)
        result = driver.find_element_by_id('swal2-title').text
        if (result == "Oops..."):
            result = driver.find_element_by_id('swal2-content').text
            
        return result
