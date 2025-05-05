import pytest
import allure
from pages.main_page import MainPage
from urls import Url


@allure.feature("Главная страница")
class TestCareerPage:
    @allure.story("Проверка загрузки главной страницы")
    @allure.suite("Загрузка страницы")
    @allure.tag("positive")
    def test_open_main_page(self, driver):
        assert driver.current_url == Url.CAREER_PAGE

    @allure.story("Проверка заголовка главной страницы")
    @allure.suite("Заголовок")
    @allure.tag("positive")
    def test_get_title_main_page(self, driver):
        assert "Карьера в IT-компании Cloud.ru" in driver.title

    @allure.story("Проверка нахождения элемента, клик по нему и редирект на другую страницу")
    @allure.suite("Переход")
    @allure.tag("positive")
    def test_click_bootcamp_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bootcamp_button()
        assert driver.current_url == Url.BOOTCAMP_PAGE


