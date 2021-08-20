from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time





class single_radio():

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
        self.driver.maximize_window()

    def push_button_gender(self, nume):
        if nume == "Male":
            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[1]/div[2]/label[1]/input")
            self.driver.execute_script("arguments[0].click();", button)
        if nume == "Female":
            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[1]/div[2]/label[2]/input")
            self.driver.execute_script("arguments[0].click();", button)

    def push_get_value(self):
        button = self.driver.find_element_by_xpath("//*[@id=\"buttoncheck\"]")
        self.driver.execute_script("arguments[0].click();", button)

    def extract_txt(self):
        elements = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]')
        msg2 = str(elements.text)

        return msg2

    def validation(self,nume,msg2):

        if nume == 'Male':
            if 'Male' in msg2:
                return True
            elif "Female" in msg2:
                print("Eroare la afisare")
                return False
            else:
                print('Nu avem un mesaj!')
                return False
        if nume == 'Female':
            if 'Female' in msg2:
                return True
            elif "Male" in msg2:
                print("Eroare la afisare")
                return False
            else:
                print('Nu avem un mesaj!')
                return False



ob = single_radio()
nume = input("Introduceti numele Male/Female: ")
ob.push_button_gender(nume)
ob.push_get_value()
msg2 = ob.extract_txt()
print(ob.validation(nume,msg2))







