from selenium.webdriver.common.by import By
from ja_lp.exercises.selenium_exercises.selElements import SeleniumPageElements

from ja_lp.utils.baseselenium import SeleniumActions


class Clickpage(SeleniumActions):
    # name of Selenium WebDriver's first result on google.
    search_result_page = (By.CLASS_NAME, 'LC20lb')

    def click_link(self):
        self.click_element(self.search_result_page)
        return SeleniumPageElements(self.driver)


