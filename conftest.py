import allure
import pytest
from urls import Url
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Url.MAIN_PAGE)
    yield driver
    driver.quit()