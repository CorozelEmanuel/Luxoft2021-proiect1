from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import Driver
import time

#Radio Button Demo
class radio_buttons_demo():

    # def __init__(self):
    #     self.driver = webdriver.Chrome('./chromedriver')
    #     self.driver.implicitly_wait(10)
    #     self.driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
    #     self.driver.maximize_window()

    def select_radio_button_demo(self):
        click_radio_button_demo = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/ul/li[3]/a')
        click_radio_button_demo.click()
        return True

    def radio_button(self, gender):
        if gender == 'Male':
            male_button = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input').click()

            click_button_value = Driver.driver.find_element(By.ID, 'buttoncheck').click()

            value = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]').text

            lista = value.split(' ')
            print(lista)
            if "'Male'" in lista:
                print('A fost afisat raspunsul corect: ', value)
            else:
                print('Nu a fost afisat raspunsul corect: ', value)

        elif gender == 'Female':
            male_button = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]/input').click()


            click_button_value = Driver.driver.find_element(By.ID, 'buttoncheck').click()

            value = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]').text

            lista = value.split(' ')
            print(lista)
            if "'Female'" in lista:
                print('A fost afisat raspunsul corect: ', value)
            else:
                print('Nu a fost afisat raspunsul corect: ', value)

        else:
            print("Genul introdus nu este corect")
            return False




#Group Radio Buttons Demo

    def group_radio_buttons(self, sex, age):
        if sex == 'Male':
            male= Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[1]/input').click()

            if age == '0 to 5':
                button1 = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input').click()
                button_get_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

                text_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text
                lista_values = text_values.split('\n')
                print(lista_values)

                if 'Male' in lista_values[0]:
                    if '0 - 5' in lista_values[1]:
                        print('Varsta aleasa este corecta')

                    else:
                        print('Varsta aleasa nu este corecta')


                else:
                    print('Genul ales nu este corect')



            elif age == '5 to 15':
                button2 = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input').click()
                button_get_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

                text_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text
                lista_values = text_values.split('\n')
                print(lista_values)

                if 'Male' in lista_values[0]:
                    if '5 - 15' in lista_values[1]:
                        print('Varsta aleasa este corecta')

                    else:
                        print('Varsta aleasa nu este corecta')

                else:
                    print('Genul ales nu este corect')


            elif age == '15 to 50':
                button3 = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input').click()
                button_get_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

                text_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text
                lista_values = text_values.split('\n')
                print(lista_values)

                if 'Male' in lista_values[0]:
                    if '15 - 50' in lista_values[1]:
                        print('Varsta aleasa este corecta')

                    else:
                        print('Varsta aleasa nu este corecta')

                else:
                    print('Genul ales nu este corect')


            else:
                print('Varsta introdusa nu este corecta')
                return False


        elif sex == 'Female':
            female= Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input').click()

            if age == '0 to 5':
                button1 = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input').click()
                button_get_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

                text_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text
                lista_values = text_values.split('\n')
                print(lista_values)

                if 'Female' in lista_values[0]:
                    if '0 - 5' in lista_values[1]:
                        print('Varsta aleasa este corecta')
                    else:
                        print('Varsta aleasa nu este corecta')

                else:
                    print('Genul ales nu este corect')


            elif age == '5 to 15':
                button2 = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input').click()
                button_get_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

                text_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text
                lista_values = text_values.split('\n')
                print(lista_values)

                if 'Female' in lista_values[0]:
                    if '5 - 15' in lista_values[1]:
                        print('Varsta aleasa este corecta')

                    else:
                        print('Varsta aleasa nu este corecta')

                else:
                    print('Genul ales nu este corect')


            elif age == '15 to 50':
                button3 = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input').click()
                button_get_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()

                text_values = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]').text
                lista_values = text_values.split('\n')
                print(lista_values)

                if 'Female' in lista_values[0]:
                    if '15 - 50' in lista_values[1]:
                        print('Varsta aleasa este corecta')

                    else:
                        print('Varsta aleasa nu este corecta')

                else:
                    print('Genul ales nu este corect')

            else:
                print('Varsta introdusa nu este corecta')

        else:
            print("Genul introdus nu este corect")
            return False



#     def tearDown(self):
#         self.driver.close()

# d = radio_buttons_demo()
# d.select_radio_button_demo()
#
# gen = input("Introduceti genul: ")
# d.radio_button(gen)
#
# sex = input ("Introduceti genul: ")
# varsta = input("Introduceti varsta: ")
# d.group_radio_buttons(sex, varsta)

# d.tearDown()


