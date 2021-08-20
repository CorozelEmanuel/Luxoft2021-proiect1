from selenium import webdriver
from main.start_web import Driver


class check_title_url():


    def check_url(self,url):
        if url == Driver.driver.get(url):
            return True
        else:
            return False

    def check_Title(self,name):

        if name == Driver.driver.title:
            return True
        else:
            return False