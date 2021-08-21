from driver import Driver
from Input_Forms import input_forms
from Simple_Form_Demo import simple_form_demo
from Checkbox_Demo import checkbox_demo
from Radio_Button_Demo import radio_buttons_demo

a = Driver()
a.go_url("https://www.seleniumeasy.com/test/")

b = input_forms()
b.click_input_forms()

c = simple_form_demo()
c.select_simple_form()
message = input("Introduceti mesajul: ")
c.single_input_field(message)
c.verify_message(message)
a=int(input("Introduceti numarul: "))
b=int(input("Introduceti numarul: "))
c.two_input_fields(a,b)
c.verify_sum(a,b)
message_a = input("Introduceti mesajul: ")
c.verify_error(message_a)

# d = checkbox_demo()
# d.select_checkbox_demo()
# d.click_single_checkbox_demo()
# d.verify_success()
# d.click_multiple_checkbox_demo()
# d.verify_checkboxes()
# d.checkbox_disabled()
# d.checkbox_enabled()
#
# e = radio_buttons_demo()
# e.select_radio_button_demo()
# gen = input("Introduceti genul: ")
# e.radio_button(gen)
# sex = input ("Introduceti genul: ")
# varsta = input("Introduceti varsta: ")
# e.group_radio_buttons(sex, varsta)

