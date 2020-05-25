import time
import json


class DiaryParams:

    def start_add(self, driver, user, test_desc):

        success_count = 0

        # login
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
        diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
        try:
            diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        diary_link.click()

        # show parameters page
        driver.find_element_by_id('parameters_btn').click()

        # add paper color
        driver.find_element_by_id('paperColor-add').click()
        description = driver.find_element_by_name('description')
        driver.implicitly_wait(2)
        description.send_keys(test_desc)
        driver.find_element_by_css_selector("button[class='menu-button btn btn-success'][type='button']").click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'The option is added.' == result:
            success_count = success_count + 1

        time.sleep(3)
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()
        
        # add paper type
        driver.find_element_by_id('paperType-add').click()
        description = driver.find_element_by_name('description')
        driver.implicitly_wait(2)
        description.send_keys(test_desc)
        driver.find_element_by_css_selector("button[class='menu-button btn btn-success'][type='button']").click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'The option is added.' == result:
            success_count = success_count + 1
        
        time.sleep(3)
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()
        
        # add cover color
        driver.find_element_by_id('coverColor-add').click()
        description = driver.find_element_by_name('description')
        driver.implicitly_wait(2)
        description.send_keys(test_desc)
        driver.find_element_by_css_selector("button[class='menu-button btn btn-success'][type='button']").click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'The option is added.' == result:
            success_count = success_count + 1

        return success_count

    def start_delete(self, driver, user):

        success_count = 0

        # login
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
        diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
        try:
            diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        diary_link.click()

        # show parameters page
        driver.find_element_by_id('parameters_btn').click()

        # add paper color
        driver.find_element_by_id('default-pc-checkbox-1').click()
        driver.find_element_by_id('pc-delete').click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'Deletion is completed successfully.' == result:
            success_count = success_count + 1

        time.sleep(3)
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()
        
        # add paper type
        driver.find_element_by_id('default-pt-checkbox-1').click()
        driver.find_element_by_id('pt-delete').click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'Deletion is completed successfully.' == result:
            success_count = success_count + 1

        time.sleep(3)
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()
        
        # add cover color
        driver.find_element_by_id('default-cc-checkbox-1').click()
        driver.find_element_by_id('cc-delete').click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'Deletion is completed successfully.' == result:
            success_count = success_count + 1
        
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()

        return success_count

    def start_recover(self, driver, user):

        success_count = 0

        # login
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
            diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
        except:
            driver.find_element_by_css_selector("button[type='button']").click()
            diary_link = driver.find_element_by_xpath('//a[@href="/admin/diary"]')
            driver.find_element_by_css_selector("button[type='button']").click()

        diary_link.click()

        # show parameters page
        driver.find_element_by_id('parameters_btn').click()

        # add paper color
        driver.find_element_by_id('default-pc-checkbox-3').click()
        driver.find_element_by_id('pc-recover').click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'Recovery is completed successfully.' == result:
            success_count = success_count + 1

        time.sleep(3)
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()
        
        # add paper type
        driver.find_element_by_id('default-pt-checkbox-3').click()
        driver.find_element_by_id('pt-recover').click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'Recovery is completed successfully.' == result:
            success_count = success_count + 1

        time.sleep(3)
        driver.find_element_by_css_selector("button[class='swal2-confirm swal2-styled'][type='button']").click()
        
        # add cover color
        driver.find_element_by_id('default-cc-checkbox-3').click()
        driver.find_element_by_id('cc-recover').click()
        
        result = driver.find_element_by_id('swal2-title').text
        if 'Recovery is completed successfully.' == result:
            success_count = success_count + 1

        return success_count
