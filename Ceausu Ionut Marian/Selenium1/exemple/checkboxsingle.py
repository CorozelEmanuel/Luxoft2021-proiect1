from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By





class check_box_single():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        self.driver.maximize_window()
    def push_button(self):
        button = self.driver.find_element_by_xpath("//*[@id=\"isAgeSelected\"]")
        self.driver.execute_script("arguments[0].click();", button)

    def extract_text(self):
        elements = self.driver.find_element(By.ID, 'txtAge')
        msg2 = str(elements.text)
        return msg2

    def validation(self, msg2):
        if msg2:
            print('Avem afisare')
            if 'Success' in msg2:
                return True
            else:
                return False
        else:
            return False
def msj_check(driver):
    button = driver.find_element_by_xpath("//*[@id=\"isAgeSelected\"]")
    driver.execute_script("arguments[0].click();", button)
    elements = driver.find_element(By.ID, 'txtAge')

    msg2 = str(elements.text)
    if msg2:
        print('Avem afisare')
        if 'Success' in msg2:
            print('Contine')
            print(msg2)
        else:
            print("Afisare incorecta!")
    else:
        print ('False')

ob = check_box_single()
ob.push_button()
msg2 = ob.extract_text()
print(ob.validation(msg2))









