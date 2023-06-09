from time import sleep
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger

# create a class for the page
class MyProfilePage(BasePage):

    # create a method that performs actions on the page
    def select_my_profile(self):
        self.driver.find_element(By.CSS_SELECTOR, ".aside__row:last-child").click()
        sleep(3)
        logger.info('Clicked on My Profile')

    # create a method that provide the my profile menus
    def get_my_profile_menus(self):
        my_profile_menu = self.driver.find_elements(By.CSS_SELECTOR, 'a.filter-container__term')
        return {menu.text.lower() for menu in my_profile_menu}
        

    