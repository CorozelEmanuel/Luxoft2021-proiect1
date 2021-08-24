from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from web_init import Driver
from verify_url_title import verify

import time
from go_to_input_forms import InputForms

import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s <%(levelname)s> - %(funcName)s : %(message)s",
                    datefmt="%H:%M%S")


class simple_form():

    def go_to_simple_form_demo(self):

        try:  # cautam simple form demo
            a = InputForms()
            a.input_forms()
            simple_form_demo = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/ul/li[1]/a')
            logging.info('s-a gasit elementul corespunzator lui go_to_simple_demo')


        except WebDriverException as e:

            logging.error('nu s-a gasit elementul corespunzator')
            Driver.driver.close()
            return False


        else:
            simple_form_demo.click()
            logging.info('s-a realizat accesarea simple_form_demo')
            time.sleep(5)
            return True


    def single_input_field(self, mesaj = 'Mesaj default'):

        try:
            enter_message = Driver.driver.find_element(By.ID, 'user-message')
            logging.info('S-a gasit elementul corespunzator pentru introducerea mesajului')
            press_show_message = Driver.driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
            logging.info('S-a gasit elemtnul corespuzator butonului de SHOW MESSAGE')


        except WebDriverException as e:
            logging.error('nu s-a gasit elementul')
            Driver.driver.close()
            return False

        else:
            enter_message.send_keys(mesaj)
            logging.info('s-a introdus mesajul in casuta corespunzatoare')
            time.sleep(5)
            press_show_message.click()
            logging.info('s-a apasat pe butonul de show message')
            enter_message.clear()  # stergem ce am introdus mai devreme in bara de mesaje pentru a putea efectua un nou test fara a da peste un test acolo
            time.sleep(5)
            return True




    def verify_single_input_field(self, mesaj = 'Mesaj default'):

        try:
            your_message = Driver.driver.find_element(By.ID, 'display')
            logging.info('S-a gasit elementul corespunzator mesajului cautat')

        except WebDriverException as e:
            logging.error('Nu s-a gasit elementul corespunzator mesajului cautat')
            Driver.driver.close()
            return False

        else:
            if your_message.get_attribute('outerText') == mesaj:
                logging.info('Mesajul afisat este unul corect')
                return True
            else:
                logging.info('Mesajul afisat este unul incorect')
                return False


    def two_input_fields(self, a = 1, b = 1):


        try:

            enter_a = Driver.driver.find_element(By.ID, 'sum1')
            enter_b = Driver.driver.find_element(By.ID, 'sum2')
            logging.info('S-au gasit elementele cautate a si b')
            press_get_total = Driver.driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
            logging.info('S-a gasit elementul corespunzator pentru botonul de get total')

        except WebDriverException as e:
            logging.error(f'Nu s-au gasit elementele cautate eroare-> {e}')
            Driver.driver.close()
            return False

        else:

            enter_a.send_keys(a)
            time.sleep(5)
            enter_b.send_keys(b)
            time.sleep(5)

            press_get_total.click()
            time.sleep(5)
            enter_a.clear()
            time.sleep(5)
            enter_b.clear()
            return True

    def verify_two_input_fields(self, a = 1, b = 1):

        try:
            total = Driver.driver.find_element(By.ID, 'displayvalue')
            logging.info('S-a gasit elementul cautat')

        except WebDriverException as e:
            logging.error(f'Nu s-au gasit elementele cautate, eroare -> {e}')
            Driver.driver.close()
            return False

        else:

            if str(a).isdigit() and str(b).isdigit():

                if (a+b) == int(total.get_attribute('outerText')):
                    logging.info('ati introdus a si b intregi iar rezultatul este unul corect')
                    return True

                else:
                    logging.info('ati introdus a si b intregi iar rezultatul este unul incorect')
                    return False

            else:

                if total.get_attribute('outerText') == 'NaN':
                    logging.info('ati introdus a si b, cel putin unul nu este intreg, iar rezultatul este unul corect')
                    return True

                else:
                    logging.info('ati introdus a si b, cel putin unul nu este intreg, iar rezultatul este unul incorect')
                    return False




