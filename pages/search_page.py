import time
import math
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .locators import SearchPageLocators

class SearchPage(BasePage):
    def should_be_yandex_url(self): # Проверяем корректность url
        try:
            assert "yandex.ru" in self.browser.current_url, "Incorrect url!"
        except (NoSuchElementException):
            return False
        return True

    def should_be_search_input(self): #Проверка наличия поля поиска 
        assert self.is_element_present(*SearchPageLocators.SEARCH_FORM), "No input for search"
    
    def enter_data_input_search(self): #Ввод в поисковую строку значения 
        text_in = self.browser.find_element(*SearchPageLocators.SEARCH_FORM)
        text_in.send_keys("тензор")

    def should_be_visibly_suggest(self, timeout=10): #Проверка наличия таблицы с подсказками (suggest)
        assert self.is_element_vision_on_page(*SearchPageLocators.SUGG_FORM), "No suggest form"

        
    def enter_on_search_form(self): #Нажатие enter, проверка наличия слова "тензор" в титуле страницы 
        self.browser.find_element(*SearchPageLocators.SEARCH_FORM).send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            assert "тензор" in self.browser.title, "Incorrect search input!"
        except (NoSuchElementException):
            return False
        return True

    def should_be_search_result(self): #Проверка наличия списка результатов
        assert self.is_element_present(*SearchPageLocators.SEARCH_RESULTS), "No search results"
    
    def should_be_tensor_in_links(self): #В первых 5 результатах есть ссылка на tensor.ru
        lists = self.browser.find_elements(*SearchPageLocators.SEARCH_LINK)
        t = "tensor.ru"
        for listitem in lists:
            href_a = listitem.get_attribute("href")
            if t in href_a:
                print(href_a.count(t))
                assert int(href_a.count(t)) >= 5, "tensor.ru присутствует не во всех пяти первых ссылках"
