from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

# importing the LoginPage class from LoginPage file
from pages.LoginPage import LoginPage

# create test cases
def test_login_page(driver):
    # check if Login text is displayed
    assert driver.find_element(By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


def test_user_login(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.user_login()
    assert login_page.text_exists('Log Out')


def test_admin_login(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.admin_login()
    assert login_page.text_exists('Log Out')


# create a list of tuples, which contains test data
invalid_login_parameters = [
    ('', 'test', 'Field is required'),
    ('aa', 'test', 'Should be minimum 4 chars'),
    ('Test', 'Test', 'Wrng username or password'),
    # ('Test', '', 'Field is required'),
    # ('*&^hj', 'IUH*&(*)', 'Wrong username or password'),
]

# create a parameterized test case
@pytest.mark.parametrize("username, password, checkpoint", invalid_login_parameters)
def test_invalid_login(driver, username, password, checkpoint):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.text_exists(checkpoint)
