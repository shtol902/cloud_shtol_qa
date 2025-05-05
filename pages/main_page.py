import allure
from locators.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step("Клик на кнопку Стажировки")
    def click_on_bootcamp_button(self):
        self.base_click_element(LocatorsMainPage.BOOTCAMP_BUTTON)

