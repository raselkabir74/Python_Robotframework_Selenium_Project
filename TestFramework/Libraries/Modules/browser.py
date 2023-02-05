
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import os.path


_driver = None
_existing_handles = []
_screenshot_count = 0
_time_out_value = 60
_current_browser = None
_download_folder_name = 'Downloads'
_execution_root_directory = None


def set_execution_directory(root_directory):
    """
    Set execution root directory
    """
    global _execution_root_directory
    _execution_root_directory = root_directory

def get_execution_directory():
    """
    get execution root directory
    """
    global _execution_root_directory
    return _execution_root_directory

def get_download_folder_directory():
    """
    get download folder directory
    """
    global _download_folder_name
    return os.path.join(os.getcwd(), _download_folder_name)


def driver():
    """
    Global variable of WebDriver
    :return: WebDriver instance
    """
    global _driver
    return _driver

def open_chrome():
    """
    Implementing launch Chrome browser functionality
    Create a new Chrome Driver instance by a dictionary of capabilities to request when
             starting the browser session.
    :return: driver instance
    """
    global _driver
    global _current_browser
    _current_browser = 'chrome'
    caps = DesiredCapabilities.CHROME
    caps['javascriptEnabled'] = True
    caps['acceptSslCerts'] = True
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    # options.add_argument("--incognito")
    options.add_argument('disable-infobars')
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")

    prefs = {"profile.default_content_settings.popups": 0,
             "profile.default_content_setting_values.notifications": 1,
             "profile.default_content_setting_values.automatic_downloads": 1,
             "profile.default_content_setting_values.geolocation": 1,
             "download.default_directory": os.path.join(os.getcwd(), _download_folder_name),
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    _driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=options, executable_path=get_driver_path('chrome'))

def goto(value):
    """
    Implementing load web page functionality
    Loads a web page in the current browser session.
    :param value: URL
    :return:
    """
    global _driver
    maximize_window()
    delete_cookies()
    _driver.get(value)

def goto_specific_url(value):
    """
    Implementing goto specific url functionality
    :param value:
    :return:
    """
    global _driver
    _driver.get(value)

def set_time_out_value(value):
    """
    Implementing set time out value functionality
    :param value: time in seconds
    :return:
    """
    global _time_out_value
    _time_out_value = value

def get_time_out_value():
    """
    Implementing get time out value functionality
    :return: time out value
    """
    global _time_out_value
    return _time_out_value

def wait(value):
    """
    Implementing web driver wait functionality
    WebDriver Wait instance
    :param value: Seconds
    :return:
    """
    global _driver, _time_out_value
    if value is not None:
        return WebDriverWait(_driver, value)
    else:
        return WebDriverWait(_driver, _time_out_value)

def maximize_window():
    """
    Implementing maximize browser window functionality
    Maximizes the current window that webdriver is using
    """
    global _driver
    _driver.maximize_window()

def delete_cookies():
    """
    Delete all cookies of browser
    Implementing delete cookies functionality
    """
    global _driver
    _driver.delete_all_cookies()
    _driver.refresh()

def refresh_window():
    """
    Implementing refresh current page functionality
    Refreshes the current page.
    """
    global _driver
    _driver.refresh()

def page_title():
    """
    Implementing get page title functionality
    Returns the title of the current page.
    """
    global _driver
    return _driver.title


def scroll_into_view(element):
    """
    Implementing scroll into view functionality
    :param element:
    :return:
    """
    global _driver
    _driver.execute_script("arguments[0].scrollIntoView(true);", element)

def close_browser():
    """
    Implementing close current window functionality
    Closes the current window.
    :return:
    """
    global _driver
    _driver.close()

def quit():
    """
    Implementing close browser functionality
    Quits the driver and closes every associated window.
    :return:
    """
    global _driver
    _driver.quit()

def capture_screenshot(directory):
    """
    Implementing capture screenshot functionality
    :return: image path
    """
    global _screenshot_count
    file_name = "screenshot_"  + str.replace(str.replace(str(datetime.datetime.now()), ' ', '_'), ':', '') + "_" + str(_screenshot_count) + ".png"
    file_path = directory + "\\" + file_name
    _driver.get_screenshot_as_file(file_path)
    _screenshot_count += 1
    return file_name

def get_driver_path(browser_name):
    """
    Implement return driver path based on browser name
    :param browser_name:
    :return:
    """
    _script_path = os.path.dirname(os.path.abspath(__file__))
    _driver_path = os.path.split(_script_path)[0]
    if(browser_name.lower() == 'chrome'):
        _browser_driver_path = os.path.join(_driver_path, 'Drivers', 'chromedriver.exe')
    elif(browser_name.lower() =='ie'):
        _browser_driver_path = os.path.join(_driver_path, 'Drivers', 'IEDriverServer.exe')
    else:
        _browser_driver_path = os.path.join(_driver_path, 'Drivers', 'geckodriver.exe')
    return _browser_driver_path

def move_to_element(element):
    """
    Implementing drag and drop functionality
    :param element:
    :return:
    """
    global _driver
    actions = ActionChains(_driver)
    actions.move_to_element(element).perform()

def script_executor_click(element, execute_async_script):
    """
    Implementing executor click functionality
    Using JavaScript Executor, click on WebElement
    :param element: WebElement locator
    :param execute_async_script:
    """
    global _driver
    if execute_async_script is True:
        pass
    _driver.execute_script("var elem=arguments[0]; setTimeout(function() {elem.click();}, 50)", element)

def every_downloads_chrome():
    global _driver
    if not _driver.current_url.startswith("chrome://downloads"):
        _driver.get("chrome://downloads/")
    return _driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)
