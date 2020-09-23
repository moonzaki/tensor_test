import time
from pages.base_page import BasePage
from pages.search_page import SearchPage

link = "https://yandex.ru/"

def test_open_yandex_search(browser): #Вход на yandex, проверка url на наличие соответствующего значения в нем
    page = SearchPage(browser, link)
    page.open()
    page.should_be_yandex_url()

def test_search_form(browser):
    #current_link = browser.current_url
    page = SearchPage(browser, link)
    page.should_be_search_input()
    page.enter_data_input_search()
    page.should_be_visibly_suggest()
    page.enter_on_search_form()

def test_search_results(browser):
#    current_link = browser.current_url
    page = SearchPage(browser, link)
    page.should_be_search_result()
    page.should_be_tensor_in_links()