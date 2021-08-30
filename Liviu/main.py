from driver import Driver
from Simple_Form_Demo import simple_form
from checkbox_demo import Checkbox_demo
from input_forms import Input_forms




a = Driver()
a.go_url("https://www.seleniumeasy.com/test/")

b = Input_forms()
b.click_input_forms()

c = simple_form()
c.simple_form_demo()
c.single_input_field()
c.verify_message()
c.two_input_fields()
c.verify_two_input()
d = Checkbox_demo()
d.checkbox_demo_click()
d.click_single_checkbox_demo()
d.verify()
d.click_multiple_checkbox_demo()
d.verify_checkboxes()
d.checkbox_disabled()
d.checkbox_enabled()


