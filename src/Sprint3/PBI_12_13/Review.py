import time
import json


class Review:

    def start(self, driver, user, order_id, option, description):
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

        driver.find_element_by_id('order_history').click()

        time.sleep(2)

        driver.find_element_by_id(order_id+'-review-btn').click()

        time.sleep(2)

        driver.find_element_by_css_selector("option[value='"+option+"']").click()
        driver.find_element_by_id('review_desc').send_keys(description)
        driver.find_element_by_id(order_id+'-submit-btn').click()

        time.sleep(2)

        result = driver.find_element_by_id('swal2-title').text

        return result
