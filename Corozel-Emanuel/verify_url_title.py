import sys

from selenium import webdriver
from web_init import Driver

class verify():

    def expected_url(self, string_url):


        if string_url == Driver.driver.current_url:

            return True

        else:
            return False


    def expected_title(self, string_title):


        if string_title == Driver.driver.title:

            return True

        else:
            return False


