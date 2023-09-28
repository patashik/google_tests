from selenium.webdriver.support.wait import WebDriverWait
import requests

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_correct_response_status_code(self):
        code = 200
        status_code = requests.get(self.browser.current_url).status_code
        assert status_code == code, "Status not correct"
