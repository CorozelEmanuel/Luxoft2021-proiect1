
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from main.start_web import Driver


class InputForms():

    def  inputforms(self):
        try:
            inputforms_button = Driver.driver.find_element(By.XPATH, '//*[@id="treemenu"]/li/ul/li[1]/i')
            print("S-a gasit elementul cautat")
        except  WebDriverException as e:
            print("Nu s-a gasit elementul cautat")
            Driver.close()
            return False
        else:
            Driver.driver.execute_script("arguments[0].click();", inputforms_button)
            return True

