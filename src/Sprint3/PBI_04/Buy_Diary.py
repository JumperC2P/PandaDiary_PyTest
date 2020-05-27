import time
import json


class Buy_Diary:

    def start(self, driver, user, cover_color, title, paper_color, paper_type, info):
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

        try:
            buy_diary_link = driver.find_element_by_xpath('//a[@href="/myDiary"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            buy_diary_link = driver.find_element_by_xpath('//a[@href="/myDiary"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        buy_diary_link.click()

        driver.execute_script('$("#'+cover_color+'").click()')
        driver.find_element_by_name('title').send_keys(title)
        driver.find_element_by_css_selector("button[type='button'][class='ui button btn btn-primary']").click()

        time.sleep(2)

        driver.execute_script('$("#'+paper_color+'").click()')
        driver.find_element_by_css_selector("option[id='"+paper_type+"']").click()
        driver.find_element_by_id('content-button-submit').click()

        time.sleep(1)

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

        driver.find_element_by_css_selector("button[type='button'][class='swal2-confirm swal2-styled'").click()

        return result
