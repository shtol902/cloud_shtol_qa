import allure
from locators.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step("Клик на кнопку Хочу на стажировку")
    def click_on_internship_button(self):
        self.base_click_element(LocatorsMainPage.WANT_TO_INTERNSHIP_BUTTON)

    @allure.step("Получить текст заголовка формы")
    def get_text_from_form_title(self):
        return self.get_text_from_element(LocatorsMainPage.INTERNSHIP_TITLE_FORM)

    @allure.step("Скролл страницы до кнопки /Карьерный портал/ в футере")
    def scroll_to_the_form(self):
        return self.scroll_to_element(LocatorsMainPage.CAREER_BUTTON)

    @allure.step("Клик на кнопку Карьерный портал")
    def click_on_career_button(self):
        self.base_click_element(LocatorsMainPage.CAREER_BUTTON)

