from selenium.webdriver.common.by import By

class SearchPageLocators():
    SEARCH_STRING = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    PREDICTION_ITEM = (By.XPATH, "//*[@id='Alh6id']/div[1]/div/ul/li[1]") 
    IMAGE_SEARCH_BUTTON = (By.CSS_SELECTOR, "div.nDcEnd")
    IMAGE_LINK_STRING = (By.XPATH, "//*[@id='ow10']/div[3]/c-wiz/div[2]/div/div[3]/div[2]/c-wiz/div[2]/input")
    IMAGE_LINK_SEARCH_BUTTON = (By.CSS_SELECTOR, "div.Qwbd3")
    UPLOAD_ELEMENT = (By.NAME, "encoded_image")
    SCREEN_KEYBOARD = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]")

class ResultPageLocators():
    SEARCH_STRING = (By.NAME, "q")
    CAT_PAW = (By.CSS_SELECTOR, "div[data-animal-type='1']")
    PAW_SCREEN = (By.CSS_SELECTOR, "canvas.GQ0mne")
    CLOSE_PAW_BUTTON = (By.CSS_SELECTOR, "div[class='XgKUwb Ke4YHe d4TAJd']")
    USELESS_BOX = (By.XPATH, "//*[@id='kp-wp-tab-overview']/div[1]/div/div/div/block-component/div/div[2]/div")