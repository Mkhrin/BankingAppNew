from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from logs.logger import logger

# importing the LoginPage class from LoginPage file
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.MyProfilePage import MyProfilePage

# create test cases
def test_my_profile_menu(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.user_login()
    sleep(5)
   
    # create an  instance of MyProfile class
    my_profile = MyProfilePage(driver)
    my_profile.select_my_profile()
    # check if My Profile text is displayed
    assert driver.find_element(By.CSS_SELECTOR, 'div.aside__row.active').text.upper() == 'MY PROFILE'




# def test_my_profile_summary_menu(driver):
#     # create an instance/object of LoginPage class
#     login_page = LoginPage(driver)
#     # call user_login method of the object
#     login_page.user_login()
#     sleep(5)
   
    # # create an  instance of MyProfile class
    # my_profile = MyProfilePage(driver)
    # my_profile.user_summary_view()
    # # check if User Information text is displayed
    # assert driver.find_element(By.CSS_SELECTOR, 'div.sub-heading').text.isinit() == 'User Information'



# def test_my_profile_menus(driver):
#     # create an instance/object of LoginPage class
#     login_page = LoginPage(driver)
#     # call user_login method of the object
#     login_page.user_login()
#     sleep(5)
#     # create an instance of HomePage class
#     my_profile = MyProfilePage(driver)
#     expected_my_profile_menus = {'summary', 'profile', 'security', 'settings', 'files'}
#     displayed_my_profile_menus = my_profile.get_my_profile_menus()
#     logger.info(f'Expected {expected_my_profile_menus}')
#     logger.info(f'Displayed {displayed_my_profile_menus}')
#     diff = expected_my_profile_menus ^ displayed_my_profile_menus
#     assert len(diff) == 0