from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from driver import Driver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time

class Checkbox_demo():

        def checkbox_demo_click(self):
            checkbox_demo = Driver.driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/ul/li[2]/a')
            checkbox_demo.click()
            time.sleep(5)
            return checkbox_demo

        def click_single_checkbox_demo(self):
            checkbox_click = Driver.driver.find_element(By.ID, 'isAgeSelected')
            checkbox_click.click()
            time.sleep(5)
            return checkbox_click

        def verify(self):
            new = Driver.driver.find_element(By.ID, 'txtAge').text
            lista = new.split()
            result = 'Succes'
            if result in lista:
                print('{}:Textul contine cuvantul Success'.format(new))
            time.sleep(3)
            return result

# multiple Checkbox Demo

        def click_multiple_checkbox_demo(self):
            button_check_all = Driver.driver.find_element(By.ID, 'check1')
            button_check_all.click()
            time.sleep(5)
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
            result1='Uncheck All'
            if self.text_button() == result1:
                print('{}: Textul butonului este corect'.format(self.text_button()))
            else:
                print('{}: Textul butonului nu este corect'.format(self.text_button()))
            time.sleep(5)
            return result1

        def checkbox_enabled(self):
            checkboxes = []
            checkboxes = Driver.driver.find_elements(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div/label/input')
            checkboxes[2].click()

            result2='Check All'
            if self.text_button() == result2:
                print('{}: Textul butonului este corect '.format(self.text_button()))
            else:
                print('{}: Textul butonului nu este corect '.format(self.text_button()))
            time.sleep(5)
            return result2