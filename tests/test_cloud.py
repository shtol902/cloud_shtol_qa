import pytest
import allure
from pages.main_page import MainPage
from urls import Url

@allure.feature("Главная страница")
class TestMainPage:
    @allure.story("Проверка загрузки главной страницы")
    @allure.suite("Загрузка страницы")
    @allure.tag("positive")
    def test_open_main_page(self, driver):
        assert driver.current_url == Url.MAIN_PAGE

    @allure.story("Проверка заголовка главной страницы")
    @allure.suite("Заголовок")
    @allure.tag("positive")
    def test_get_title_main_page(self, driver):
        assert "Стажировка Cloud.ru Camp" in driver.title

    @allure.story("Проверка заголовка формы, после клика на кнопку")
    @allure.suite("Заголовок")
    @allure.tag("positive")
    def test_get_title_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_internship_button()
        assert main_page.get_text_from_form_title() == 'Заполни заявку и стань частью команды Cloud.ru'

    @allure.story("Проверка перехода на другую страницу по клику")
    @allure.suite("Переход")
    @allure.tag("positive")
    def test_redirect_career_page(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_element()
        main_page.click_on_career_button()
        assert driver.current_url == Url.CAREER_PAGE