from selenium import webdriver
from driver import Driver
from Input_Forms import input_forms
from Checkbox_Demo import checkbox_demo
from Radio_Button_Demo import radio_buttons_demo

a = Driver()
a.go_url("https://www.seleniumeasy.com/test/")

b=input_forms()
b.click_input_forms()

c= checkbox_demo()
c.select_checkbox_demo()
c.click_single_checkbox_demo()
c.verify_success()
c.click_multiple_checkbox_demo()
c.verify_checkboxes()
c.checkbox_disabled()
c.checkbox_enabled()

# d = radio_buttons_demo()
# d.select_radio_button_demo()
# gen = input("Introduceti genul: ")
# d.radio_button(gen)
# sex = input ("Introduceti genul: ")
# varsta = input("Introduceti varsta: ")
# d.group_radio_buttons(sex, varsta)


