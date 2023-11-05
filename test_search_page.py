import pytest
import time
import os
from .pages.search_page import SearchPage
from .pages.result_page import ResultPage
import allure

@pytest.mark.chrome
@allure.epic("Search Page")
@allure.feature("Essential features")
@allure.parent_suite("Chrome tests for search page")
@allure.suite("Tests for essential features")
class TestHappyPathChrome():
    @allure.title("Text search by button")
    @allure.story("Text search by button")
    @allure.sub_suite("Tests for text search")
    def test_should_start_search_by_text_and_button(self, browser_chrome):
        search_request = "тестирование"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text and activate search"):
            browser_chrome.implicitly_wait(5) 
            search_page.start_search_by_button(search_request)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)
   
    @allure.title("Text search by enter")
    @allure.story("Text search by enter")
    @allure.sub_suite("Tests for text search")
    def test_should_start_search_by_text_and_enter(self, browser_chrome):
        search_request = "тестирование"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text and activate search"):
            browser_chrome.implicitly_wait(5) 
            search_page.start_search_by_press_enter(search_request)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)

    @allure.title("Text search using screen keyboard")
    @allure.story("Text search using screen keyboard")
    @allure.sub_suite("Tests for text search") 
    def test_should_start_search_by_screen_keyboard_and_button(self, browser_chrome):
        search_request = "тестирование"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text and activate search"):
            browser_chrome.implicitly_wait(5) 
            search_page.start_search_by_screen_keyboard(search_request)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)

    @pytest.mark.predict
    @allure.title("Text search by prediction")
    @allure.story("Text search by prediction")
    @allure.sub_suite("Tests for prediction search")
    def test_should_start_search_by_prediction(self, browser_chrome):
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: choose prediction and activate search"):
            browser_chrome.implicitly_wait(5) 
            prediction_item = search_page.choose_prediction()
            prediction_content = prediction_item.get_attribute("aria-label")
            print(f"это подсказка - {prediction_content}")
            prediction_item.click()
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_prediction_in_search_string(prediction_content)

    @pytest.mark.imagefile
    @allure.title("Image search using file")
    @allure.story("Image search using file")
    @allure.sub_suite("Tests for image search")
    def test_should_start_search_by_image_file(self, browser_chrome):
        link = "https://www.google.com/"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_data', 'test_image.jpg')
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: upload file and activate search"):
            browser_chrome.implicitly_wait(5)
            search_page.start_search_by_image_file(file_path) 
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_open_lens_page()
            result_page.should_be_correct_response_status_code()
            
    @allure.title("Image search using link and button")
    @allure.story("Image search using link and button")
    @allure.sub_suite("Tests for image search")
    def test_should_start_search_by_image_link_and_button(self, browser_chrome):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert link and activate search"):
            browser_chrome.implicitly_wait(5) 
            search_page.start_search_by_image_link_and_button(image_link)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_open_lens_page()
            result_page.should_be_correct_response_status_code()
            
    @allure.title("Image search using link and enter")
    @allure.story("Image search using link and enter")
    @allure.sub_suite("Tests for image search")
    def test_should_start_search_by_image_link_and_enter(self, browser_chrome):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert link and activate search"):
            browser_chrome.implicitly_wait(5) 
            search_page.start_search_by_image_link_and_enter(image_link)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_open_lens_page()
            result_page.should_be_correct_response_status_code()
            
    @allure.title("Cat search")
    @allure.story("Text search using cat paws")
    @allure.sub_suite("Tests to see cat paws") 
    def test_cat(self, browser_chrome):
        search_request = "international cat day"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_chrome, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert link and activate search"):
            browser_chrome.implicitly_wait(5) 
            search_page.start_search_by_press_enter(search_request)
        with allure.step("Step 3: go to search result page and enjoy cat paws"):
            search_page.url_changed()
            result_page = ResultPage(browser_chrome, browser_chrome.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_click_cat_paw()
            result_page.should_close_cat_paw()

@pytest.mark.firefox
@allure.epic("Search Page")
@allure.feature("Essential features")
@allure.parent_suite("Firefox tests for search page")
@allure.suite("Tests for essential features")
class TestHappyPathFirefox():
    @allure.title("Text search by button")
    @allure.story("Text search by button")
    @allure.sub_suite("Tests for text search")
    def test_should_start_search_by_text_and_button(self, browser_firefox):
        search_request = "тестирование"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text and activate search"):
            browser_firefox.implicitly_wait(5) 
            search_page.start_search_by_button(search_request)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)

    @allure.title("Text search by enter")
    @allure.story("Text search by enter")
    @allure.sub_suite("Tests for text search")
    def test_should_start_search_by_text_and_enter(self, browser_firefox):
        search_request = "тестирование"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text and activate search"):
            browser_firefox.implicitly_wait(5) 
            search_page.start_search_by_press_enter(search_request)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)
    
    @pytest.mark.key
    @allure.title("Text search using screen keyboard")
    @allure.story("Text search using screen keyboard")
    @allure.sub_suite("Tests for text search") 
    def test_should_start_search_by_screen_keyboard_and_button(self, browser_firefox):
        search_request = "тестирование"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text and activate search"):
            browser_firefox.implicitly_wait(5) 
            search_page.start_search_by_screen_keyboard(search_request)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)

    @pytest.mark.predict
    @allure.title("Text search by prediction")
    @allure.story("Text search by prediction")
    @allure.sub_suite("Tests for prediction search")
    def test_should_start_search_by_prediction(self, browser_firefox):
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: choose prediction and activate search"):
            browser_firefox.implicitly_wait(5) 
            prediction_item = search_page.choose_prediction()
            prediction_content = prediction_item.get_attribute("aria-label")
            print(f"это подсказка - {prediction_content}") #на случай падения теста
            prediction_item.click()
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_prediction_in_search_string(prediction_content)

    @allure.title("Image search using file")
    @allure.story("Image search using file")
    @allure.sub_suite("Tests for image search")
    def test_should_start_search_by_image_file(self, browser_firefox):
        link = "https://www.google.com/"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_data', 'test_image.jpg')
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: upload file and activate search"):
            browser_firefox.implicitly_wait(5)
            search_page.start_search_by_image_file(file_path) 
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_open_lens_page()
            result_page.should_be_correct_response_status_code()

    @allure.title("Image search using link and button")
    @allure.story("Image search using link and button")
    @allure.sub_suite("Tests for image search")
    def test_should_start_search_by_image_link_and_button(self, browser_firefox):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert link and activate search"):
            browser_firefox.implicitly_wait(5) 
            search_page.start_search_by_image_link_and_button(image_link)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_open_lens_page()
            result_page.should_be_correct_response_status_code()
            
    @allure.title("Image search using link and enter")
    @allure.story("Image search using link and enter")
    @allure.sub_suite("Tests for image search")
    def test_should_start_search_by_image_link_and_enter(self, browser_firefox):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert link and activate search"):
            browser_firefox.implicitly_wait(5) 
            search_page.start_search_by_image_link_and_enter(image_link)
        with allure.step("Step 3: go to search result page"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_open_lens_page()
            result_page.should_be_correct_response_status_code()
            
    @allure.title("Cat search")
    @allure.story("Text search using cat paws")
    @allure.sub_suite("Tests to see cat paws") 
    def test_cat(self, browser_firefox):
        search_request = "international cat day"
        link = "https://www.google.com/"
        with allure.step("Step 1: open main page"):
            search_page = SearchPage(browser_firefox, link)
            search_page.open()
            search_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert link and activate search"):
            browser_firefox.implicitly_wait(5) 
            search_page.start_search_by_press_enter(search_request)
        with allure.step("Step 3: go to search result page and enjoy cat paws"):
            search_page.url_changed()
            result_page = ResultPage(browser_firefox, browser_firefox.current_url)
            result_page.should_be_correct_response_status_code()
            result_page.should_be_search_request_in_search_string(search_request)
            result_page.should_click_cat_paw()
            result_page.should_close_cat_paw()