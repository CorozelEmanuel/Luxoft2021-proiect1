
from main.start_web import Driver
from web.check_title_url import check_title_url
from web.imput_fileds import simple_form
from web.radio_buttons import radio
from web.input_forms import InputForms
a = Driver()

a.go_to_page("https://www.seleniumeasy.com/test/")

b = check_title_url()
b.check_url("https://www.seleniumeasy.com/test/")

c = InputForms()

c.inputforms()


d = simple_form()
d.go_to_page()
d.single_input_fileds("Ana are mere")
d.verify_single("Ana are mere")
d.two_input_fields(1,2)
d.verify_two_input(1,2)


c.inputforms()

e = radio()
e.go_to_page()
e.single_radio('Male')
e.verify_single_radio('Male')
e.multi_radio('Male', 4)
print(e.verify_multi('Male', 4))