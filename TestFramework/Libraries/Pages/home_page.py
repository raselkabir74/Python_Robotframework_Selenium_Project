"""Implementing Home Screen Page objects repository"""

from TestFramework.Libraries.Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Start: Home page locators
    guide_link_locator = (By.XPATH, "//A[text()='Guide']")
    logout_button_locator = (By.XPATH, "//i[@class='g-icon g-icon_header-dropdown']")
    # End: Home page locators

    def is_login_successful(self):
        """
        Implementing is login successful functionality
        :return: True/False
        """
        is_successful = self.is_element_present(self.guide_link_locator, time_out=30)
        return is_successful

    def search_with_specific_keyword(self, keyword):
        """
        Implementing search with specific keyword functionality
        :param keyword:
        :return:
        """
        search_box_locator = (By.XPATH, "//input[@name='q']")
        self.set_value_into_input_field(search_box_locator, keyword)
        # self.click_element(search_box_locator, error_message="search box not found before specified time out", wait_after_click=True)
