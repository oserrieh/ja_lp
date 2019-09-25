from selenium.webdriver.common.by import By
from ja_lp.utils.baseselenium import SeleniumActions
from ja_lp.exercises.selenium_exercises.clickPage import Clickpage


class GooglePageElements(SeleniumActions):
    # search box from Google home page
    search_field = (By.NAME, 'q')
    # Name of the I'm Feeling Lucky box
    feeling_lucky = (By.NAME, 'btnI')
    # the class name for "search by mic"
    mic_search = (By.CLASS_NAME, 'hb2Smf')
    # "Google Search" button class name
    search_box_button = (By.CLASS_NAME, 'gNO89b')
    # Google apps square dots near google account
    square_dots = (By.CLASS_NAME, 'gb_B')

    def check_search_element_present(self):
        return self.is_element_present(self.search_field)

    def check_lucky_present(self):
        return self.presence_of_element(self.feeling_lucky)

    def check_mic_search(self):
        return self.is_element_present(self.mic_search)

    def check_searchbox_present(self):
        return self.presence_of_element(self.search_box_button)

    def check_square_dots(self):
        return self.presence_of_element(self.square_dots)

    def search_string(self):
        self.google_search(self.search_field)
        return Clickpage(self.driver)

    def google_search(self, element):
        elem = self.get_element(element)
        elem.send_keys('Selenium WebDriver')
        elem.submit()
