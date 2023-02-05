"""Implementing Home UI Page Actions"""

from selenium.common.exceptions import WebDriverException
from TestFramework.Libraries.logger import Logger
from TestFramework.Libraries.Pages.home_page import HomePage


class Home:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    logger = Logger().get_logger('Home')

    def __init__(self):
        self._home_page = HomePage()

    def is_login_successful(self):
        """
        Returning user login success status
        Implementing logging for is login successful functionality
        :return: True/False
        """
        try:
            self.logger.info('Start: is login successful')
            return self._home_page.is_login_successful()
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            raise
        finally:
            self.logger.info('End: is login successful')

    def search_with_specific_keyword(self, keyword):
        """
        Returning search with specific keyword
        Implementing logging for search with specific keyword functionality
        :param keyword:
        :return: True/False
        """
        is_select = None
        try:
            self.logger.info('Start: search with specific keyword')
            self._home_page.search_with_specific_keyword(keyword)
            is_select = True
        except WebDriverException as exp:
            is_select = False
            self.logger.error(exp.msg)
            raise
        finally:
            self.logger.info('End: search with specific keyword')
            return is_select