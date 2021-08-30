from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from driver import Driver
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
wait_time_out = 15

#1 single input field

class simple_form():

    def simple_form_demo(self):
            time.sleep(5)
            simple_form = Driver.driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/ul/li[1]/a')
            simple_form.click()
            time.sleep(5)
            return simple_form

    def single_input_field(self, cuvant = 'mesaj'):
            enter_message = Driver.driver.find_element(By.ID, 'user-message')
            press_show_message = Driver.driver.find_element(By.XPATH, '//*[@id="get-input"]/button')

            enter_message.send_keys(cuvant)
            time.sleep(3)
            press_show_message.click()
            enter_message.clear()
            time.sleep(3)
            return cuvant


    def verify_message(self, cuvant = 'mesaj'):

        output_message = Driver.driver.find_element(By.XPATH,'//*[@id="display"]').text
        if output_message == cuvant:
            print("{}: Mesajul afisat este corect".format(output_message))
            return True
        else:
            print("{}: Mesajul afisat nu este corect".format(output_message))
            return False

#2 two input fields

    def two_input_fields(self, a= 5, b= 7):
        press_get_total = Driver.driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
        enter_a = Driver.driver.find_element(By.ID, 'sum1')
        enter_a.send_keys(a)
        time.sleep(1)
        enter_b = Driver.driver.find_element(By.ID, 'sum2')
        enter_b.send_keys(b)
        time.sleep(1)
        press_get_total.click()
        time.sleep(5)
        enter_a.clear()
        enter_b.clear()
        time.sleep(1)
        return True

    def verify_two_input(self, a = 5, b = 7):
        try:
            total = Driver.driver.find_element(By.ID, 'displayvalue')
            print('S-a gasit elementul cautat')

        except WebDriverException as e:
            print(f'Nu s-au gasit elementele cautate, eroare -> {e}')
            Driver.driver.close()


        else:

            if str(a).isdigit() and str(b).isdigit():

                if (a+b) == int(total.get_attribute('outerText')):
                    print('ati introdus a si b intregi iar rezultatul este unul corect')


                else:
                    print('ati introdus a si b intregi iar rezultatul este unul incorect')


            else:

                if total.get_attribute('outerText') == 'NaN':
                    print('ati introdus a si b, cel putin unul nu este intreg, iar rezultatul este unul corect')


                else:
                    print('ati introdus a si b, cel putin unul nu este intreg, iar rezultatul este unul incorect')


