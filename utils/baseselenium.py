from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from ja_lp.utils.base_testcase import BaseTestCase

class SeleniumActions(BaseTestCase):

    test_case = BaseTestCase(self.driver)
    driver = test_case.driver
    timeout_time = 5

    wait = WebDriverWait(test_case.driver, timeout_time)

    def get_element(self, selector):
        element = self.wait.until(ec.visibility_of_element_located(selector))
        return element

    def is_element_present(self, selector):
        try:
            element = self.wait.until(ec.visibility_of_element_located(selector))
            return element.is_displayed()
        except TimeoutException:
            return False

    def click_element(self, element):
        elem = self.wait.until(ec.element_to_be_clickable(element))
        elem.click()





