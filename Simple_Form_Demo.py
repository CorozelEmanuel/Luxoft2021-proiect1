from selenium.webdriver.common.by import By
from driver import Driver
import time
import logging

#Single Input Field

class simple_form_demo():

    def select_simple_form(self):
        click_simple_form_demo = Driver.driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/ul/li[1]/a')
        click_simple_form_demo.click()
        time.sleep(5)
        return click_simple_form_demo

    def single_input_field(self, message):
        enter_message = Driver.driver.find_element(By.ID, 'user-message')
        show_message_button = Driver.driver.find_element(By.CLASS_NAME, 'btn-default')
        enter_message.send_keys(message)
        time.sleep(5)
        show_message_button.click()
        enter_message.clear()
        time.sleep(5)

        return message


    def verify_message(self, message):

        output_message = Driver.driver.find_element(By.XPATH,'//*[@id="display"]').text
        if output_message == message:
            print("{}: Mesajul afisat este corect".format(output_message))
            return True
        else:
            print("{}: Mesajul afisat nu este corect".format(output_message))
            return False


#Two Input Fields

    def two_input_fields(self,a,b):

        enter_a = Driver.driver.find_element(By.XPATH,'//*[@id="sum1"]')
        enter_a.send_keys(a)
        time.sleep(5)

        enter_b = Driver.driver.find_element(By.XPATH , '//*[@id="sum2"]')
        enter_b.send_keys(b)
        time.sleep(5)

        get_total_button= Driver.driver.find_element(By.XPATH,'//*[@id="gettotal"]/button')
        get_total_button.click()
        time.sleep(5)

        enter_a.clear()
        enter_b.clear()
        time.sleep(5)

        return True


    def verify_sum(self,a,b):
        total = Driver.driver.find_element(By.ID, 'displayvalue').text
        sum = 0
        sum = str(a + b)
        if total == sum:
            print("{}: Mesajul afisat este corect".format(total))
            return True
        else:
            print("{}: Mesajul afisat nu este corect".format(total))
            return False


    def verify_error(self, message_a):

        enter_a = Driver.driver.find_element(By.XPATH, '//*[@id="sum1"]')
        enter_a.send_keys(message_a)
        time.sleep(5)

        get_total_button = Driver.driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
        get_total_button.click()
        time.sleep(5)

        total = Driver.driver.find_element(By.ID, 'displayvalue').text

        if total == 'NaN':
            print("Eroarea afisata este cea corecta")
            return True
        else:
            print("Eroarea afisata nu este cea corecta")
            return False

