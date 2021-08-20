from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class two_input_fields():
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        self.driver.maximize_window()

    def put_nr(self, nr1, nr2):
        nr1_box = self.driver.find_element_by_id('sum1').send_keys(nr1)

        nr2_box = self.driver.find_element_by_id('sum2').send_keys(nr2)

    def push_button(self):
        button = self.driver.find_element_by_xpath("//*[@id=\"gettotal\"]/button")
        self.driver.execute_script("arguments[0].click();", button)

    def extract_sum(self):
        elements = self.driver.find_element(By.ID, 'displayvalue')

        sum2 = str(elements.text)
        return sum2

    def check_sum(self, nr1, nr2):
        elements = self.driver.find_element(By.ID, 'displayvalue')

        sum2 = str(elements.text)
        for i in range(1):
            if sum2 == "NaN":
                print("Nu au fost introduse numere!")
                break

        sum = 0
        sum = int(nr1) + int(nr2)
        if str(sum) == sum2:
            return True
        else:
            return False



ob = two_input_fields()

nr1 = input('Enter your number : ')
nr2 = input('Enter your number : ')
ob.put_nr(nr1,nr2)
ob.push_button()
if(ob.extract_sum()== 'NaN'):
    print("Numerele introduse nu sunt numere")
if (ob.check_sum(nr1,nr2)):
    print("Numerele au fost introduse corect")
print(ob.check_sum(nr1,nr2))




