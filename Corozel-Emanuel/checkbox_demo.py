from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from web_init import Driver
from verify_url_title import verify
import time

class Checkbox():

    def go_to_checkbox_demo(self):

        try:
            go_to_checkbox = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/ul/li[2]/a')

        except WebDriverException as e:
            Driver.close_session()
            return False

        else:
            go_to_checkbox.click()
            time.sleep(5)
            return True


    def single_checkbox_demo(self, alegere = 'bifeaza'): # daca e orice altceva decat bifeaza -> va debifa

        try:
            click_single_checkbox = Driver.driver.find_element(By.ID, 'isAgeSelected')
            time.sleep(5)

        except WebDriverException as e:
            Driver.close_session()
            return False

        else:

            if alegere.lower() == 'bifeaza':
                if click_single_checkbox.is_selected():
                    return True

                else:
                    click_single_checkbox.click()
                    time.sleep(5)
                    return True

            else:
                if click_single_checkbox.is_selected():
                    click_single_checkbox.click()
                    time.sleep(5)
                    return True

                else:
                    return True

    def verify_single_checbox_demo(self, alegere = 'bifeaza'):

        try:
            verify_single_checkbox = Driver.driver.find_element(By.ID, 'txtAge')

        except WebDriverException as e:
            Driver.close_session()
            return False

        else:
            if alegere.lower() == 'bifeaza':
                if verify_single_checkbox.get_attribute('style') == "display: block;":
                    return True

                else:
                    return False

            else:

                if verify_single_checkbox.get_attribute('style') == "display: none;":
                    return True

                else:
                    return False

    def lista_cu_checkbox(self): # functie care ne returneaza o lista cu cele 4 chechbox pentru a le putea prelucra in late functii
        try:
            lista_butoane = Driver.driver.find_elements(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div/label/input')
            time.sleep(5)
        except WebDriverException as e:
            Driver.close_session()
            return False
        else:
            return lista_butoane

    def bifeaza_multiple_checkbox_demo(self, *optiuni):


        try:
            lista = self.lista_cu_checkbox()

            for i in optiuni:    # pentru un for de la 1 la 4, verificam fiecare checkbox daca este in optiunile alese, daca da ->verificam deca este dezactvat si il activam
                if i in (1, 2, 3, 4):                                                                                                          #  daca nu -> verificam daca este activat si il activam
                    if not lista[i-1].is_selected():
                        lista[i-1].click()
        except:
            return False

        else:
            return True

    def verifica_apasare_butoane(self, *optiuni):

        s = 0
        try:
            lista = self.lista_cu_checkbox()

            for i in optiuni:
                if lista[i-1].is_selected():
                    s += 1
        except:
            return False

        else:
            if s == len(optiuni):
                return True

            else:
                return False





    def debifeaza_multiple_checkbox_demo(self, *optiuni):

        lista = self.lista_cu_checkbox()

        try:
            lista = self.lista_cu_checkbox()

            for i in optiuni:
                if i in (1, 2, 3, 4):
                    if lista[i - 1].is_selected():
                        lista[i - 1].click()
        except:
            return False

        else:
            return True


    def verify_multiple_checkbox_demo(self, *optiuni): #aici vom trimite ce checboxu ri sunt bifate si vom verifica textul te pe buton

        lista = self.lista_cu_checkbox()
        suma = 0

        try:
            buton_verificare = Driver.driver.find_element(By.ID, 'check1')

        except WebDriverException as e:
            Driver.close_session()
            return False

        else:

            text = buton_verificare.get_attribute('value')
            for i in range(4):
                if lista[i].is_selected():
                    suma += 1

            if suma == 4 and text == 'Uncheck All':
                return True

            elif suma < 4 and text == 'Check All':
                return True

            else:
                return False


















