from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s <%(levelname)s> - %(funcName)s : %(message)s",
                    datefmt="%H:%M%S")

class Driver():

    driver = None

    def __init__(self):
        logging.info('s-a creat o sesiune de selenium-chrome')
        Driver.driver = webdriver.Chrome('C:\\Users\\Manu\\PycharmProjects\\chromedriver')
        Driver.driver.maximize_window()
        time.sleep(7)


    def go_to_url(self, url):

        self.url = url
        Driver.driver.get(url)
        logging.info(f's-a realizat navigarea la url-ul ---> {url}')
        time.sleep(7)
        if url == "https://www.seleniumeasy.com/test/":

            x_button = Driver.driver.find_element(By.ID, 'at-cv-lightbox-close')
            x_button.click()

    def close_session(self):

        if Driver.driver:
            Driver.driver.close()
            logging.info('S-a inchis sesiunea de selenium')




