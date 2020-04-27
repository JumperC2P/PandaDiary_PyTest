
import time
import json


class Register():

    def start(self, driver, user, is_checked):
        try:
            register_link = driver.find_element_by_link_text('Register')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            register_link = driver.find_element_by_link_text('Register')
            driver.find_element_by_css_selector("button[type='button']").click()

        register_link.click()
        user_link = driver.find_element_by_link_text('User')
        user_link.click()
        driver.find_element_by_name('username').send_keys(user['username'])
        driver.find_element_by_name('email').send_keys(user['email'])
        driver.find_element_by_name('password').send_keys(user['password'])
        driver.find_element_by_name('confirmPassword').send_keys(user['confirmed_password'])
        if (is_checked):
            driver.find_element_by_name('terms').click()
        submit_button = driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        time.sleep(2)
        result = driver.find_element_by_id('swal2-title').text
        if (result == "Oops..."):
            result = driver.find_element_by_id('swal2-content').text
            
        return result

        