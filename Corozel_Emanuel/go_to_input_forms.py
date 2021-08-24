from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from web_init import Driver
import time

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s <%(levelname)s> - %(funcName)s : %(message)s",
                    datefmt="%H:%M%S")

class InputForms():



    def input_forms(self):

        try:  # cautam input_forms si apasam pe al pentru a vedea variantele pe care le putem alege
            input_forms_click = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/i')
            logging.info('element gasit cu succes')

        except WebDriverException as e:
            logging.error('nu s-a gasit input Forms')
            Driver.driver.close()
            return False

        else:
            input_forms_click.click()
            logging.info('s-a realizat apasarea pe input forms')
            time.sleep(5)
            return True




