from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Driver():

    driver = None

    def __init__(self):
        Driver.driver = webdriver.Chrome('C:\\Users\\40799\\PycharmProjects\\Selenium1\\chromedriver')
        #Driver.driver.maximize_window()
        time.sleep(7)

    def go_to_page(self, url):
        self.url = url
        Driver.driver.get(url)
        time.sleep(7)

    def close_session(self):
        if Driver.driver:
            Driver.driver.close()