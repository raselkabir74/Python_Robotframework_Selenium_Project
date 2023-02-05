"""Implements Test Startup settings"""

import TestFramework.Libraries.Modules.browser as Browser


class TestFixture:
    """
    Set webdriver time out value function
    Launching/Navigating System Under Test
    Closing browser instance
    Implement capture screenshot
    Set test environment function
    Returning test data for a test suit
    Writing test data into excel file
    """

    def set_execution_directory(self, root_directory):
        """
        Set execution root directory
        """
        Browser.set_execution_directory(root_directory)

    def setup(self, browser_name):
        browser = None
        if (browser_name.lower() == 'chrome'):
            browser = Browser.open_chrome()
        return browser

    def set_time_out_value(self, value):
        """
        Implementing set webdriver time out value functionality
        :param value: time out value in seconds
        :return:
        """
        try:
            Browser.set_time_out_value(60)
            if value != None and value != "":
                time_out_value = int(value)
                if time_out_value > 0:
                    Browser.set_time_out_value(time_out_value)
        except:
            Browser.set_time_out_value(60)

    def goto(self, value):
        """Launching/Navigating System Under Test"""
        return Browser.goto(value)

    def teardown(self):
        """Closing browser instance"""
        return Browser.quit()

    def capture_screenshot(self, directory):
        """ Implement capture screenshot """
        return Browser.capture_screenshot(directory)
