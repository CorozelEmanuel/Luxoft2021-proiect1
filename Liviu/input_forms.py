from selenium.webdriver.common.by import By
from driver import Driver
import time

class Input_forms():


    def click_input_forms(self):
        click_input = Driver.driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/a')
        click_input.click()
        time.sleep(5)
        return click_input