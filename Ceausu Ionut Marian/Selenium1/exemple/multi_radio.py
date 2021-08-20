from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class multi_radio():

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
        self.driver.maximize_window()

    def push_gender_button(self,name):
        if name == "Male":
            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[1]/label[1]/input")
            self.driver.execute_script("arguments[0].click();", button)
        if name == "Female":
            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input")
            self.driver.execute_script("arguments[0].click();", button)

    def push_age_button(self, age):

        if age>=0 and age <5:

            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input")
            self.driver.execute_script("arguments[0].click();", button)

        elif age>=5 and age <15:

            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input")
            self.driver.execute_script("arguments[0].click();", button)
        elif age >= 15 and age < 50:

            button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input")
            self.driver.execute_script("arguments[0].click();", button)

    def push_get_values(self):

        button = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/button")
        self.driver.execute_script("arguments[0].click();", button)

    def extract_gender(self):

        founded = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/p[2]").text.split('\n')
        msg2 = founded[0]
        return msg2

    def extract_age(self):

        founded = self.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/p[2]").text.split('\n')
        msg3 = founded[1]
        return msg3

    def validation(self,nume, msg2,age,msg3):
        if nume == 'Male':
            if 'Male' in msg2:
                if age >= 0 and age < 5:
                    if '0 - 5' in msg3:
                        return True
                elif age >= 5 and age < 15:
                    if '5 - 15' in msg3:
                        return True
                elif age >= 15 and age < 50:
                    if '15 - 50' in msg3:
                        return True
        if nume == 'Female':
            if 'Female' in msg2:
                if age >= 0 and age < 5:
                    if '0 - 5' in msg3:
                        return True
                elif age >= 5 and age < 15:
                    if '5 - 15' in msg3:
                        return True
                elif age >= 15 and age < 50:
                    if '15 - 50' in msg3:
                        return True
    def close(self):
        self.driver.close()











age=[]
nume = []
for i in range(3):
    msg = input('Introduceti o varsta de la 0 la maxim 50 : ')
    age.append(int(msg))
    msg2 = input('Introduceti sexul Male/Female : ')
    nume.append(msg2)
for i in range(3):
    ob = multi_radio()
    ob.push_gender_button(nume[i])
    ob.push_age_button(age[i])
    ob.push_get_values()
    msg2 = ob.extract_gender()
    msg3 = ob.extract_age()
    print(ob.validation(nume[i],msg2,age[i],msg3))
    ob.close()