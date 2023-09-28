from .base_page import BasePage
from .locators import SearchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):
    def choose_prediction(self):
        search_string = self.browser.find_element(*SearchPageLocators.SEARCH_STRING)
        search_string.click()
        prediction_item = self.browser.find_element(*SearchPageLocators.PREDICTION_ITEM)
        return prediction_item

    def start_search_by_button(self, search_request):
        search_string = self.browser.find_element(*SearchPageLocators.SEARCH_STRING)
        search_string.send_keys(search_request)
        search_button = self.browser.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_button.click()

    def start_search_by_image_file(self, file_path):
        image_search_button = self.browser.find_element(*SearchPageLocators.IMAGE_SEARCH_BUTTON)
        image_search_button.click()
        upload_element = self.browser.find_element(*SearchPageLocators.UPLOAD_ELEMENT)
        upload_element.send_keys(file_path)
    
    def start_search_by_image_link_and_button(self, image_link):
        image_search_button = self.browser.find_element(*SearchPageLocators.IMAGE_SEARCH_BUTTON)
        image_search_button.click()
        image_link_string = self.browser.find_element(*SearchPageLocators.IMAGE_LINK_STRING)
        image_link_string.send_keys(image_link)
        image_link_search_button = self.browser.find_element(*SearchPageLocators.IMAGE_LINK_SEARCH_BUTTON)
        image_link_search_button.click()
        
    def start_search_by_image_link_and_enter(self, image_link):
        image_search_button = self.browser.find_element(*SearchPageLocators.IMAGE_SEARCH_BUTTON)
        image_search_button.click()
        image_link_string = self.browser.find_element(*SearchPageLocators.IMAGE_LINK_STRING)
        image_link_string.send_keys(image_link)
        image_link_string.send_keys(Keys.ENTER)

    def start_search_by_prediction(self):
        search_string = self.browser.find_element(*SearchPageLocators.SEARCH_STRING)
        search_string.click()
        prediction = self.browser.find_element(*SearchPageLocators.PREDICTION_ITEM)
        prediction.click()
    
    def start_search_by_press_enter(self, search_request):
        search_string = self.browser.find_element(*SearchPageLocators.SEARCH_STRING)
        search_string.send_keys(search_request)
        search_string.send_keys(Keys.ENTER)
        

    

