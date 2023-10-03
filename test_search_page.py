import pytest
import time
import os
from .pages.search_page import SearchPage
from .pages.result_page import ResultPage

@pytest.mark.chrome
class TestHappyPathChrome():
    def test_should_start_search_by_text_and_button(self, browser_chrome):
        search_request = "тестирование"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5) 
        search_page.start_search_by_button(search_request)
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_search_request_in_search_string(search_request)

    def test_should_start_search_by_text_and_enter(self, browser_chrome):
        search_request = "тестирование"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5) 
        search_page.start_search_by_press_enter(search_request)
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_search_request_in_search_string(search_request)

    def test_should_start_search_by_prediction(self, browser_chrome):
        link = "https://www.google.com/"
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5) 
        prediction_item = search_page.choose_prediction()
        prediction_content = prediction_item.text
        print(f"это подсказка - {prediction_content}")
        prediction_item.click()
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_prediction_in_search_string(prediction_content)

    def test_should_start_search_by_image_file(self, browser_chrome):
        link = "https://www.google.com/"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_image.jpg')
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5)
        search_page.start_search_by_image_file(file_path) 
        time.sleep(5)
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_open_lens_page()

    def test_should_start_search_by_image_link_and_button(self, browser_chrome):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5) 
        search_page.start_search_by_image_link_and_button(image_link)
        time.sleep(5)
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_open_lens_page()

    def test_should_start_search_by_image_link_and_enter(self, browser_chrome):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5) 
        search_page.start_search_by_image_link_and_enter(image_link)
        time.sleep(5)
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_open_lens_page()
    
    @pytest.mark.cat    
    def test_cat(self, browser_chrome):
        search_request = "international cat day"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_chrome, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_chrome.implicitly_wait(5) 
        search_page.start_search_by_press_enter(search_request)
        result_page = ResultPage(browser_chrome, browser_chrome.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_search_request_in_search_string(search_request)
        browser_chrome.implicitly_wait(5) 
        result_page.should_click_cat_paw()
        result_page.should_close_cat_paw()
        
@pytest.mark.firefox
class TestHappyPathFirefox():
    @pytest.mark.xfail(reason="search gives 2 buttons - one inactive")
    def test_should_start_search_by_text_and_button(self, browser_firefox):
        search_request = "тестирование"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_firefox, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_firefox.implicitly_wait(5) 
        search_page.start_search_by_button(search_request)
        result_page = ResultPage(browser_firefox, browser_choosen.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_search_request_in_search_string(search_request)

    def test_should_start_search_by_text_and_enter(self, browser_firefox):
        search_request = "тестирование"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_firefox, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_firefox.implicitly_wait(5) 
        search_page.start_search_by_press_enter(search_request)
        result_page = ResultPage(browser_firefox, browser_firefox.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_search_request_in_search_string(search_request)

    def test_should_start_search_by_prediction(self, browser_firefox):
        link = "https://www.google.com/"
        search_page = SearchPage(browser_firefox, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_firefox.implicitly_wait(5) 
        prediction_item = search_page.choose_prediction()
        prediction_content = prediction_item.text
        print(f"это подсказка - {prediction_content}") #на случай падения теста
        prediction_item.click()
        result_page = ResultPage(browser_firefox, browser_firefox.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_be_prediction_in_search_string(prediction_content)

    def test_should_start_search_by_image_file(self, browser_firefox):
        link = "https://www.google.com/"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_image.jpg')
        search_page = SearchPage(browser_firefox, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_firefox.implicitly_wait(5)
        search_page.start_search_by_image_file(file_path) 
        time.sleep(5)
        result_page = ResultPage(browser_firefox, browser_firefox.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_open_lens_page()

    def test_should_start_search_by_image_link_and_button(self, browser_firefox):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_firefox, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_firefox.implicitly_wait(5) 
        search_page.start_search_by_image_link_and_button(image_link)
        time.sleep(5)
        result_page = ResultPage(browser_firefox, browser_firefox.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_open_lens_page()

    def test_should_start_search_by_image_link_and_enter(self, browser_firefox):
        image_link = "https://images.unsplash.com/photo-1639676347575-15b1e60ab6c2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2952&q=80"
        link = "https://www.google.com/"
        search_page = SearchPage(browser_firefox, link)
        search_page.open()
        search_page.should_be_correct_response_status_code()
        browser_firefox.implicitly_wait(5) 
        search_page.start_search_by_image_link_and_enter(image_link)
        time.sleep(5)
        result_page = ResultPage(browser_firefox, browser_firefox.current_url)
        result_page.should_be_correct_response_status_code()
        result_page.should_open_lens_page()
