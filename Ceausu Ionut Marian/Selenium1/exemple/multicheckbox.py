from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class multi_check_box():

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        self.driver.maximize_window()

    def push_check_all(self):
        button = self.driver.find_element_by_xpath("//*[@id=\"check1\"]")
        self.driver.execute_script("arguments[0].click();", button)
        print("Am apasat butonul check all")


    def verify_state(self):
        org = self.driver.find_element_by_xpath('//*[@id="check1"]')
        val2 = org.get_attribute("value")
        print("Starea butonului este " + val2)


    def validation(self):
        list = ["//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[1]/label/input",
                "//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label/input",
                "//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[3]/label/input",
                "//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[4]/label/input"]
        count = 1
        for i in list:
            org = self.driver.find_element_by_xpath('//*[@id="check1"]')
            val = org.get_attribute("value")
            if val == 'Uncheck All':
                print("Ne aflam la optiunea " + str(count))
                button = self.driver.find_element_by_xpath(i)
                self.driver.execute_script("arguments[0].click();", button)
                print("Am dezactivat butonul " + str(count))
                org = self.driver.find_element_by_xpath('//*[@id="check1"]')

                val = org.get_attribute("value")
                print("Starea butonului este " + val)
                if val == 'Check All':
                    print("Optiunea" + " " + str(count) + " a fost bifata bine")
                    button = self.driver.find_element_by_xpath(i)
                    self.driver.execute_script("arguments[0].click();", button)
                    print("Am rebifat optiunea " + str(count))
                    org = self.driver.find_element_by_xpath('//*[@id="check1"]')

                    val = org.get_attribute("value")
                    print("Starea butonului este " + val)
                    print("Trecem la urmatoarea optiune")
                else:
                    print("Eroare a butonului check all ori a optiunii " + str(count))
                    break
                count += 1
            else:
                print("eroare a butonului check all")
                break
                count += 1
        print("Comportamentul butoanelor este cel dorit")






ob = multi_check_box()
ob.push_check_all()
ob.verify_state()
ob.validation()