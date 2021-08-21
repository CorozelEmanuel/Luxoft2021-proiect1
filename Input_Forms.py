from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import Driver
import time

class input_forms():


    def click_input_forms(self):
        click_input = Driver.driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/a')
        click_input.click()
        return click_input



