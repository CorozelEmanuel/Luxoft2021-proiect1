from selenium import webdriver

from web_init import Driver
from verify_url_title import verify
from go_to_input_forms import InputForms
from simple_form_demo import simple_form
from checkbox_demo import Checkbox

a = Driver()
a.go_to_url("https://www.seleniumeasy.com/test/")

b = verify()

b.expected_url("https://www.seleniumeasy.com/te/")

c = InputForms()
c.input_forms()

d = simple_form()
d.go_to_simple_form_demo()
d.single_input_field()
d.verify_single_input_field()
d.two_input_fields()
d.verify_two_input_fields()


e = Checkbox()
e.go_to_checkbox_demo()
e.single_checkbox_demo('Bifeaza')
e.single_checkbox_demo()
e.single_checkbox_demo('d')
e.verify_single_checbox_demo('d')
e.bifeaza_multiple_checkbox_demo(2, 3)
e.debifeaza_multiple_checkbox_demo(3)
e.verify_multiple_checkbox_demo()

c.single_input_field()