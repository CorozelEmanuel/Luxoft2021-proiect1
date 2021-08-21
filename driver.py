from selenium import webdriver
import time


class Driver():
    driver = None

    def __init__(self):
        Driver.driver = webdriver.Chrome('./chromedriver')
        Driver.driver.maximize_window()
        time.sleep(5)

    def go_url(self, url):
        self.url = url
        Driver.driver.get(url)
        time.sleep(5)

    def tearDown(self):
        if Driver.driver:
            Driver.driver.close()
