from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_element_and_find_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def base_click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.wait_element_and_find_element(locator).click()

    def get_text_from_element(self, locator):
        return self.wait_element_and_find_element(locator).text

    def scroll_to_element(self, locator):
        element = self.wait_element_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
