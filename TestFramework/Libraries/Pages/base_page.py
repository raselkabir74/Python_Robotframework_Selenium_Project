"""Base Page implementations"""

import TestFramework.Libraries.Modules.browser as Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException, WebDriverException

import time
import datetime
import random
import string

class BasePage:


    def wait(self, value=None):
        """
        Implementing wait functionality
        :param value: Seconds
        :return:WebDriver Wait instance
        """
        return Browser.wait(value)

    def maximize_window(self):
        """
        Implementing maximize window functionality
        Maximizes the current window that webdriver is using
        :return: Window Maximize
        """
        Browser.maximize_window()

    def refresh_window(self):
        """
        Implementing refresh window functionality
        :return: Refreshes the current page.
        """
        Browser.refresh_window()

    def close_browser(self):
        """
        Implementing close browser functionality
        :return: Closes the current window.
        """
        Browser.close_browser()

    def find_element(self, locator):
        """
        Implementing find element functionality
        :param locator:
        :param type:
        :return:
        """
        type = locator[0]
        locator = locator[1]
        element = None
        if type.lower() == "xpath":
            element = self._driver().find_element_by_xpath(locator)
        elif type.lower() == "id":
            element = self._driver().find_element_by_id(locator)
        elif type.lower() == "name":
            element = self._driver().find_element_by_name(locator)
        return element

    def is_element_present(self, locator, time_out=Browser.get_time_out_value()):
        """
        Implementing is element present functionality
        Verify WebElement locator in page/ui
        :param locator: WebElement locator
        :return: True/False
        """
        is_present = None
        try:
            self.wait(time_out).until(EC.presence_of_element_located(locator), 'locator not found before specified time out')
            is_present = True
        except:
            is_present = False
        finally:
            return is_present

    def set_value_into_input_field(self, input_field_locator, value):
        """
        Implementing set value into input field functionality
        :param input_field_locator:
        :param value:
        :return:
        """
        element = self.wait().until(EC.presence_of_element_located(input_field_locator))
        self.click_element(input_field_locator)
        element.clear()
        element.send_keys(value)

    def script_executor_click(self, element, execute_async_script=False):
        """
        Implementing script executor click functionality
        :param element: WebElement locator
        :param execute_async_script:
        :return: Click on WebElement using JavaScript Executor,
        """
        Browser.script_executor_click(element, execute_async_script)

    def click_element(self, locator, script_executor=False, error_message=None, scroll_into_view=False, time_out=60, wait_after_click=False, wait_time=3):
        """
        Implementing click element functionality
        :param locator:
        :param script_executor:
        :param error_message:
        :param scroll_into_view:
        :param wait_after_click:
        :param wait_time:
        :param time_out:
        :return:
        """
        if error_message is None or error_message == "":
            error_message = 'locator not found before specified time out'
        element = self.wait(time_out).until(EC.presence_of_element_located(locator), error_message)
        if scroll_into_view:
            self.scroll_into_view(element)
        if script_executor:
            self.script_executor_click(element)
            if wait_after_click:
                self.wait_for_ajax_spinner_load(wait_time)
        else:
            element.click()
            if wait_after_click:
                self.wait_for_ajax_spinner_load(wait_time)

    def get_text_from_element(self, locator, is_a_input_field=False):
        """
        Implementing get text from element functionality
        :return: element's text
        :param locator:
        :param is_a_input_field:
        """
        element = self.wait().until(EC.presence_of_element_located(locator), 'locator not found before specified time out')
        if is_a_input_field is True:
            text = str(element.get_attribute("value")).strip()
        else:
            text = str(element.text).strip()
        return text

    def goto_specific_url(self, value):
        """
        Implementing go to specific url functionality
        :param value:
        :return:
        """
        Browser.goto_specific_url(value)

    def is_element_visible(self, locator, timeout=30):
        """
        Implementing is element visible functionality
        Verify WebElement locator is visible in page/ui
        :param locator: WebElement locator
        :return: True/False
        """
        is_visible = None
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator), 'locator not found before specified time out')
            is_visible = True
        except:
            is_visible = False
        return is_visible

    def get_time_out_value(self):
        """
        Implementing get time out value functionality
        :return: time out value
        """
        return Browser.get_time_out_value()

    def move_to_element(self, locator):
        """
        Implementing move to element functionality
        :param locator:
        :return:
        """
        element = self.find_element(locator)
        Browser.move_to_element(element)

    def scroll_into_view(self, element):
        """
        Implementing scroll into view functionality
        :param element: WebElement
        """
        Browser.scroll_into_view(element)

    def _driver(self):
        """
        Implementing driver method
        :return: webdriver instance
        """
        return Browser.driver()

    def get_execution_directory(self):
        """
        Get execution root directory
        """
        return Browser.get_execution_directory()

    def get_download_folder_directory(self):
        """
        Get download folder directory
        """
        return Browser.get_download_folder_directory()

    def wait_for_ajax_spinner_load(self, timeout=60, ajax_spinner_locator=None, wait_time=3):
        """
        Implementing wait for ajax spinner load functionality
        Wait until Ajax Spinner exists on UI. Once it is disappear, exit from loop
        Default time out value up to 60 secs
        :param timeout:
        :param ajax_spinner_locator:
        :param time_out:
        :return:
        """
        try:
            if ajax_spinner_locator is not None:
                ajax_spinner_load_locator = ajax_spinner_locator
            else:
                ajax_spinner_load_locator = (By.XPATH, "//div[@class='loader']")
            ajax_spinner_control = self.wait(wait_time).until(EC.visibility_of_all_elements_located(ajax_spinner_load_locator), 'ajax spinner load locator not found before specified time out')
            end_time = time.time() + timeout
            flag = False
            while len(ajax_spinner_control) > 0:
                ajax_spinner_control = self.wait(wait_time).until(EC.visibility_of_all_elements_located(ajax_spinner_load_locator), 'ajax spinner load locator not found before specified time out')
                if flag:
                    break
                if time.time() > end_time:
                    break

        except TimeoutException:
            pass
        except NoSuchElementException:
            pass
        except ElementNotVisibleException:
            pass
        except WebDriverException:
            pass

    def set_value_into_specific_input_field(self, field_label_name, value, is_a_textarea=False):
        """
        Implementing set value into specific input field functionality
        :param field_label_name:
        :param value:
        :param is_a_textarea:
        """
        input_field_locator = (By.XPATH, "//label[contains(text(), '" + field_label_name + "')]/..//input | //span[contains(text(), '" + field_label_name + "')]/..//input")
        if is_a_textarea:
            input_field_locator = (By.XPATH, "//label[contains(text(), '" + field_label_name + "')]/..//textarea")
        self.set_value_into_input_field(input_field_locator, value)
        self.wait_for_ajax_spinner_load(wait_time=1)


