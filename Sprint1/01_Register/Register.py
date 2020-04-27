from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
import time
import json


class Register():

    def __init__(self):
        chrome_options = Options()
        print (pathlib.Path().absolute())
        self.driver = webdriver.Chrome(executable_path=((str)(pathlib.Path().absolute()))+'/chromedriver', chrome_options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://pandadiary.ts.r.appspot.com")


    def start(self, user):
        driver = self.driver
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
        driver.find_element_by_name('confirmPassword').send_keys(user['password'])
        driver.find_element_by_name('terms').click()
        submit_button = driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        time.sleep(2)
        result = driver.find_element_by_id('swal2-title')
        return result.text
        

# if __name__ == '__main__':
#     user = {
#         'username': 'Testing',
#         'email': 'testing@gmail.com',
#         'password': '12345678'
#     }
#     print (Register().start(user))