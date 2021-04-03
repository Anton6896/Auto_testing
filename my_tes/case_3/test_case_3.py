from selenium import webdriver
from pathlib import Path

from my_tes.case_3.pages.page_simple_form import SimpleForm, TwoInputsForm

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMEDRIVER = BASE_DIR.joinpath('chromedriver')


def test_simple_form():
    driver = webdriver.Chrome(CHROMEDRIVER)
    driver.get('https://www.seleniumeasy.com/test/')
    form_lnk = SimpleForm(driver)
    t_value = form_lnk.goto_simple_form() \
        .set_value_simple_form('valTest') \
        .submit_simple_form() \
        .get_output_simple_form()

    assert t_value == 'valTest'
    driver.close()


def test_two_inputs():
    driver = webdriver.Chrome(CHROMEDRIVER)
    driver.get('https://www.seleniumeasy.com/test/')
    """ must be an integers ::  output = (a+b)"""
    form_link = TwoInputsForm(driver)
    t_value = form_link.goto_simple_form().set_values(2, 2).submit().get_output()
    assert t_value == '4'
    driver.close()
