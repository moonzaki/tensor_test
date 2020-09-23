from selenium.webdriver.common.by import By

class SearchPageLocators():
    SEARCH_FORM = (By.CSS_SELECTOR, "#text")
    SUGG_FORM = (By.CSS_SELECTOR, ".mini-suggest__popup")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".main__content")
    SEARCH_LINK = (By.CSS_SELECTOR, ".link.organic__url")