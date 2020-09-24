from .base_page import BasePage
from .locators import PicturePageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class PicturePage(BasePage):
    def should_be_picture_link(self):
        assert self.is_element_present(*PicturePageLocators.PICTURE_LINK), "No link for pictures on page" #2 Ссылка «Картинки» присутствует на странице 

    def open_picture_link(self): #3 Кликаем на ссылку 
        pic_link = self.browser.find_element(*PicturePageLocators.PICTURE_LINK)
        pic_link.click()

    def check_url(self): #4 Проверить, что перешли на url https://yandex.ru/images/ 
        try:
            new_window = self.browser.window_handles[1]
            self.browser.switch_to.window(new_window) 
            assert "https://yandex.ru/images/" in self.browser.current_url, "Incorrect url in addres bar!"
        except (NoSuchElementException):
            return False
        return True

    def get_category(self): #5 Открыть 1 категорию, проверить что открылась, в поиске верный текст 
        first_cat = self.browser.find_element(*PicturePageLocators.FIRST_CATEGORY)
        cat_atr = first_cat.get_attribute("data-grid-text")
        first_cat.click()
        element = self.browser.execute_script("let input = document.querySelector('input');return (input.value);")
        assert cat_atr == element, "В поиске не верный текст"
        if element in self.browser.current_url:
            return True
        else:
            return False

    def open_first_picture(self): #6 Открыть 1 картинку , проверить что открылась 
        fpic = self.browser.find_element(*PicturePageLocators.FIRST_PICT)
        fpic.click()
        assert self.is_element_present(*PicturePageLocators.OPEN_PIC), "No open picture"
        #is present element

    def should_be_next_and_should_be_back(self): 
        #7 При нажатии кнопки вперед  картинка изменяется 
        #8 При нажатии кнопки назад картинка изменяется 
        #на изображение из шага 6. Необходимо проверить, что это то же изображение.
        button_next = self.browser.find_element(*PicturePageLocators.NEXT_BUTTON)
        first_picture = self.browser.find_element(*PicturePageLocators.PIC_STYLE).get_attribute("src")
        button_next.click()
        next_picture = self.browser.find_element(*PicturePageLocators.PIC_STYLE).get_attribute("src")
        assert first_picture != next_picture, "The picture has not changed"
        button_back = self.browser.find_element(*PicturePageLocators.BACK_BUTTON)
        button_back.click()
        back_picture = self.browser.find_element(*PicturePageLocators.PIC_STYLE).get_attribute("src")
        if back_picture == first_picture:
            return True
        else:
            return False
        
   