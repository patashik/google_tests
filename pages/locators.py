from selenium.webdriver.common.by import By

class SearchPageLocators():
    SEARCH_STRING = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    PREDICTION_ITEM = (By.XPATH, "//*[@id='Alh6id']/div[1]/div/ul/li[1]") 
    IMAGE_SEARCH_BUTTON = (By.CSS_SELECTOR, "div.nDcEnd")
    IMAGE_LINK_STRING = (By.CSS_SELECTOR, "input.cB9M7")
    IMAGE_LINK_SEARCH_BUTTON = (By.CSS_SELECTOR, "div.Qwbd3")
    UPLOAD_ELEMENT = (By.NAME, "encoded_image")
    
class ResultPageLocators():
    SEARCH_STRING = (By.NAME, "q")

