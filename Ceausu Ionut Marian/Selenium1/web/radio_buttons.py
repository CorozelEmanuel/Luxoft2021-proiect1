
from main.start_web import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException



class radio():

    def go_to_page(self):
        try:
            button = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/ul/li[3]/a')
            print("S-a gasit elementul cautat")

        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            Driver.driver.execute_script("arguments[0].click();", button)

    def single_radio(self,nume):
        try:
            button_male = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[1]/div[2]/label[1]/input")
            button_female = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[1]/div[2]/label[2]/input")
            get_value = Driver.driver.find_element_by_xpath("//*[@id=\"buttoncheck\"]")
            print("S-au gasit elementele cautate")
        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            if nume == 'Male':
                Driver.driver.execute_script("arguments[0].click();", button_male)
                Driver.driver.execute_script("arguments[0].click();", get_value)
            if nume == 'Female':
                Driver.driver.execute_script("arguments[0].click();", button_female)
                Driver.driver.execute_script("arguments[0].click();", get_value)

    def verify_single_radio(self,nume):
        try:
            get_text = Driver.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]')
            print('S-a gasit elementul cautat')
        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            msg2 = str(get_text.text)
            if nume == 'Male':
                if 'Male' in msg2:
                    return True
                elif "Female" in msg2:
                    print("Eroare la afisare")
                    return False
                else:
                    print('Nu avem un mesaj!')
                    return False
            if nume == 'Female':
                if 'Female' in msg2:
                    return True
                elif "Male" in msg2:
                    print("Eroare la afisare")
                    return False
                else:
                    print('Nu avem un mesaj!')
                    return False

    def multi_radio(self, name, age):
        try:
            male_button = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[1]/label[1]/input")
            female_button = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input")
            age0_5_button = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input")
            age5_15_button= Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input")
            age15_50_button= Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input")
            get_value = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/button")
            print("S-au gasit toate elementele")
        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            if name == 'Male':
                Driver.driver.execute_script("arguments[0].click();", male_button)
                if age >= 0 and age < 5:
                    Driver.driver.execute_script("arguments[0].click();", age0_5_button)
                    Driver.driver.execute_script("arguments[0].click();", get_value)
                    return True
                elif age >= 5 and age < 15:
                    Driver.driver.execute_script("arguments[0].click();", age5_15_button)
                    Driver.driver.execute_script("arguments[0].click();", get_value)
                    return True
                elif age >= 15 and age < 50:
                    Driver.driver.execute_script("arguments[0].click();", age15_50_button)
                    Driver.driver.execute_script("arguments[0].click();", get_value)
                    return True
            elif name == 'Female':
                Driver.driver.execute_script("arguments[0].click();", female_button)
                if age >= 0 and age < 5:
                    Driver.driver.execute_script("arguments[0].click();", age0_5_button)
                    Driver.driver.execute_script("arguments[0].click();", get_value)
                    return True
                elif age >= 5 and age < 15:
                    Driver.driver.execute_script("arguments[0].click();", age5_15_button)
                    Driver.driver.execute_script("arguments[0].click();", get_value)
                    return True
                elif age >= 15 and age < 50:
                    Driver.driver.execute_script("arguments[0].click();", age15_50_button)
                    Driver.driver.execute_script("arguments[0].click();", get_value)
                    return True




    def verify_multi(self, name, age):
        try:
            extract_gender_age = Driver.driver.find_element_by_xpath("//*[@id=\"easycont\"]/div/div[2]/div[2]/div[2]/p[2]").text.split('\n')

            print("S-au gasit elementele cautate" )

        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            name_extract = extract_gender_age[0]
            age_extract = extract_gender_age[1]

            if name == 'Male':
                if 'Male' in name_extract:
                    if age >= 0 and age < 5:
                        if '0 - 5' in age_extract:
                            return True
                    elif age >= 5 and age < 15:
                        if '5 - 15' in age_extract:
                            return True
                    elif age >= 15 and age < 50:
                        if '15 - 50' in age_extract:
                            return True
            if name == 'Female':
                if 'Female' in name_extract:
                    if age >= 0 and age < 5:
                        if '0 - 5' in age_extract:
                            return True
                    elif age >= 5 and age < 15:
                        if '5 - 15' in age_extract:
                            return True
                    elif age >= 15 and age < 50:
                        if '15 - 50' in age_extract:
                            return True
