from .base_page import BasePage
from .search_page import SearchPage
from .locators import ResultPageLocators
from selenium.webdriver.common.by import By
import requests

class ResultPage(BasePage):
    def should_be_search_request_in_search_string(self, search_request):
        search_string = self.browser.find_element(*ResultPageLocators.SEARCH_STRING)
        assert search_request in search_string.text, "Search string does not match initial search request"
    
    def start_search_by_button(self, search_request):
        search_string = self.browser.find_element(*SearchPageLocators.SEARCH_STRING)
        search_string.send_keys(search_request)
        search_button = self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_button.click()

    def should_be_prediction_in_search_string(self, prediction_content):
        search_string = self.browser.find_element(*ResultPageLocators.SEARCH_STRING)
        print(f"а это строка поиска - {search_string.text}") #на случай падения теста
        assert prediction_content in search_string.text, "Search request does not match prediction"
        
    def should_open_lens_page(self):
        lens_url = "https://lens.google.com/"
        assert lens_url in self.url, "Image search did not start"
