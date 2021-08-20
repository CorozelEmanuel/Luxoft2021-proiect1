

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class single_input_field():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        self.driver.maximize_window()


    def put_text(self, msg):
        msg_box = self.driver.find_element_by_class_name("form-control").send_keys(msg)
        return msg_box

    def push_button(self):
        button = self.driver.find_element_by_xpath("//*[@id=\"get-input\"]/button")
        self.driver.execute_script("arguments[0].click();", button)

    def validation(self, msg):
        elements = self.driver.find_element(By.ID, 'display')

        msg2 = str(elements.text)
        if msg == msg2:
            return True
        else:
            return False









ob = single_input_field()
msg = input('Enter your message : ')
print(ob.put_text(msg))
ob.push_button()
print(ob.validation(msg))
