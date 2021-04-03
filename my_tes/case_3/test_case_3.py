from selenium import webdriver
from pathlib import Path

from my_tes.case_3.pages.page_simple_form import SimpleForm

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMEDRIVER = BASE_DIR.joinpath('chromedriver')


def test_simple_form():
    driver = webdriver.Chrome(CHROMEDRIVER)
    driver.get('https://www.seleniumeasy.com/test/')
    form = SimpleForm(driver)
    t_value = form.goto_simple_form() \
        .set_value_simple_form('valTest') \
        .submit_simple_form() \
        .get_output_simple_form()

    assert t_value == 'valTest'
