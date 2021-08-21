from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import Driver
import time


#Single Chechbox Demo
class checkbox_demo():

    # def __init__(self):
    #     self.driver = webdriver.Chrome('./chromedriver')
    #     self.driver.implicitly_wait(10)
    #     self.driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
    #     self.driver.maximize_window()

    def select_checkbox_demo(self):
        click_checkbox_demo = Driver.driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/ul/li[2]/a')
        click_checkbox_demo.click()
        # return click_checkbox_demo

    def click_single_checkbox_demo(self):
        click_checkbox = Driver.driver.find_element(By.ID, 'isAgeSelected')
        click_checkbox.click()
        return click_checkbox


    def verify_success(self):
        text_nou = Driver.driver.find_element(By.ID, 'txtAge').text
        lista = text_nou.split()
        result = 'Succes'
        if result in lista:
            print('{}:Textul returnat contine cuvantul Success'.format(text_nou))
        return result


#Multiple Checkbox Demo

    def click_multiple_checkbox_demo(self):
        button_check_all = Driver.driver.find_element(By.ID, 'check1')
        button_check_all.click()
        return button_check_all

    def verify_checkboxes(self):
        checkboxes = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div/label/input')
        print(checkboxes.is_selected())
        return checkboxes

    def text_button(self):
        button = Driver.driver.find_element(By.XPATH, "//input[@type = 'button']")
        return button.get_attribute('value')

    def checkbox_disabled(self):
        checkboxes = []
        checkboxes = Driver.driver.find_elements(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div/label/input')
        checkboxes[2].click()
        result1='Check All'
        if self.text_button() == result1:
            print('{}: Textul butonului este corect'.format(self.text_button()))
        else:
            print('{}: Textul butonului nu este corect'.format(self.text_button()))
        return result1

    def checkbox_enabled(self):
        checkboxes = []
        checkboxes = Driver.driver.find_elements(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div/label/input')
        checkboxes[2].click()
        result2='Uncheck All'
        if self.text_button() == result2:
            print('{}: Textul butonului este corect '.format(self.text_button()))
        else:
            print('{}: Textul butonului nu este corect  '.format(self.text_button()))
        return result2


    # def tearDown(self):
    #     self.driver.close()


# c = checkbox_demo()
# c.click_single_checkbox_demo()
# c.verify_success()
# c.click_multiple_checkbox_demo()
# c.verify_checkboxes()
# c.checkbox_disabled()
# c.checkbox_enabled()
# c.tearDown()
