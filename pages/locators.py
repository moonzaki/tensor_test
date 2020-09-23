from selenium.webdriver.common.by import By

class SearchPageLocators():
    SEARCH_FORM = (By.CSS_SELECTOR, "#text")
    SUGG_FORM = (By.CSS_SELECTOR, ".mini-suggest__popup")
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".main__content")
    SEARCH_LINK = (By.CSS_SELECTOR, ".link.organic__url")

class PicturePageLocators():
    PICTURE_LINK = (By.XPATH,'//a[@data-id="images"]')
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    FIRS_CATEGORY_LINK = (By.CSS_SELECTOR, ".Link.PopularRequestList-Preview")
    INPUT_FORM = (By.CSS_SELECTOR, ".search2__input")
    FIRST_PICT = (By.CSS_SELECTOR, ".serp-item__link")
    OPEN_PIC = (By.CSS_SELECTOR, ".MMImageWrapper")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    BACK_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    PIC_STYLE = (By.CSS_SELECTOR, ".MMImage-Preview")