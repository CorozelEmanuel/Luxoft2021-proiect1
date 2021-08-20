
from main.start_web import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

class simple_form():

    def go_to_page(self):
        try:
            button = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/ul/li[1]/a')
            print("S-a gasit elementul cautat")

        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            Driver.driver.execute_script("arguments[0].click();", button)

    def single_input_fileds(self, msj):
        try:
            put_message = Driver.driver.find_element_by_class_name("form-control")
            push_button = Driver.driver.find_element_by_xpath("//*[@id=\"get-input\"]/button")
            print('elementele cautate s au gasit')
        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            put_message.send_keys(msj)
            Driver.driver.execute_script("arguments[0].click();", push_button)
            return True
    def verify_single(self, msj):
        try:
            elements = Driver.driver.find_element(By.ID, 'display')
            print("S-a gasit elementul cautat")
        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            msg2 = str(elements)

            if msg2 == msj:
                return True
            else:
                return False


    def two_input_fields(self, nr1, nr2):

        try:
            nr1_box = Driver.driver.find_element_by_id('sum1')
            nr2_box = Driver.driver.find_element_by_id('sum2')
            push_button = Driver.driver.find_element_by_xpath("//*[@id=\"gettotal\"]/button")
            print("Elementele cautate au fost gasite")

        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False

        else:
            nr1_box.send_keys(nr1)
            nr2_box.send_keys(nr2)
            Driver.driver.execute_script("arguments[0].click();", push_button)
            return True

    def verify_two_input(self, nr1, nr2):

        try:
            sum = Driver.driver.find_element(By.ID, 'displayvalue')
            print("S-a gasit elementul cautat")

        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False

        else:
            sum2 = str(sum.text)

            if str(nr1).isdigit() and str(nr2).isdigit():

                if str(nr1 + nr2) == sum2:
                    return True
                else:
                    return False
            else:
                if sum2 == 'NaN':
                    return True
                else:
                    return False
