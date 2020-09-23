import time
from pages.base_page import BasePage
from pages.picture_page import PicturePage

link ="https://yandex.ru"

def test_open(browser):
    page = PicturePage(browser, link)
    page.open()

def test_check_picture_link(browser):
    page = PicturePage(browser, link)
    page.should_be_picture_link()
    page.open_picture_link()
    page.is_window_open()
    #time.sleep(5)

def test_check_url(browser):
    page = PicturePage(browser, link)
    page.check_url()

def test_category(browser):
    page = PicturePage(browser, link)
    page.get_category()
    
def test_picture_next_and_back(browser):
    page = PicturePage(browser, link)
    page.open_first_picture()
    page.should_be_next_and_should_be_back()
    page.should_be_back()