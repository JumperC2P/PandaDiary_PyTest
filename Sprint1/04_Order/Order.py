import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path


WEB_URL = "http://localhost:3000/payment"

class Order():

    def start(self, driver, info):

        driver.find_element_by_css_selector("input[type='radio'][value='"+info['payment_option']+"']").click()
        driver.find_element_by_name("cardNumber").send_keys(info['card_number'])
        driver.find_element_by_name("expiredDateM").send_keys(info['expired_date_m'])
        driver.find_element_by_css_selector("option[value='"+info['expired_date_m']+"']").click()
        driver.find_element_by_name("securityNumber").send_keys(info['security_code'])

        driver.find_element_by_css_selector("option[value='"+info['delivery_option']+"']").click()

        name = driver.find_element_by_name("name")
        driver.execute_script("arguments[0].value = ''", name)
        name.send_keys(info['username'])
        phone = driver.find_element_by_name("phone")
        driver.execute_script("arguments[0].value = ''", phone)
        phone.send_keys(info['phone'])
        address = driver.find_element_by_name("address")
        driver.execute_script("arguments[0].value = ''", address)
        address.send_keys(info['address'])

        driver.find_element_by_id("checkout").click()

        time.sleep(2)

        result = driver.find_element_by_id('swal2-title').text

        print (result)
        driver.find_element_by_css_selector("button[type='button'][class='swal2-confirm swal2-styled'").click()

        return result


# if __name__ == "__main__":
#     Order().start()