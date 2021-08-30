from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Driver():
    driver = None

    def __init__(self):
        Driver.driver = webdriver.Chrome(r'C:\Users\livac\OneDrive\Desktop\chromedriver.exe')
        Driver.driver.maximize_window()
        time.sleep(5)

    def go_url(self, url):
        self.url = url
        Driver.driver.get(url)
        time.sleep(5)
        if url == "https://www.seleniumeasy.com/test/":

            x_button = Driver.driver.find_element(By.ID, 'at-cv-lightbox-close')
            x_button.click()

    def close_page(self):
        if Driver.driver:
            Driver.driver.close()