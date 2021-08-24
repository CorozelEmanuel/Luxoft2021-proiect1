import unittest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from web_init import Driver
import time
from verify_url_title import verify
from go_to_input_forms import InputForms
from simple_form_demo import simple_form
from checkbox_demo import Checkbox


import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s <%(levelname)s> - %(funcName)s : %(message)s",
                    datefmt="%H:%M%S")

class Testare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        i = 0
        ob1 = Driver()
        ob1.go_to_url("https://www.seleniumeasy.com/test/")


    def test_inputForms(self):
        ob2 = InputForms()
        self.assertEqual(ob2.input_forms(), True)
        logging.info('input-forms')

    def test_SimpleFormDemo(self):

        ob3 = simple_form()
        self.assertEqual(ob3.go_to_simple_form_demo(), True)
        self.assertEqual(ob3.single_input_field(), True)
        self.assertEqual(ob3.verify_single_input_field(), True)
        self.assertEqual(ob3.two_input_fields(2, 2), True)
        self.assertEqual(ob3.verify_two_input_fields(2, 2), True)
        logging.info('simpe-form')


    def test_CheckBox(self):

        ob4 = Checkbox()
        self.assertEqual(ob4.go_to_checkbox_demo(), True)
        self.assertEqual(ob4.single_checkbox_demo('bifeaza'), True)
        self.assertEqual(ob4.verify_single_checbox_demo('bifeaza'), True)
        self.assertEqual(ob4.bifeaza_multiple_checkbox_demo(1, 2), True)
        self.assertEqual(ob4.verify_multiple_checkbox_demo(1, 2), True)



        logging.info('checkbox')


    @classmethod
    def tearDownClass(cls):

        Driver.driver.close()


