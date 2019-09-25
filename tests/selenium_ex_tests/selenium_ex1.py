import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class SearchText(unittest.TestCase):
    # search box from Google home page
    search_field = (By.NAME, 'q')
    # Name of the I'm Feeling Lucky box
    feeling_lucky = (By.NAME, 'btnI')
    # the class name for "search by mic"
    mic_search = (By.CLASS_NAME, 'hb2Smf')
    # "Google Search" button class name
    search_box_button = (By.CLASS_NAME, 'gNO89b')
    # Google apps square dots near google account
    square_dots = (By.CLASS_NAME, 'gb_C')
    # the footer logo from selenium WebDiver site
    footer_logo = (By.ID, 'footerLogo')
    # Class name of Selenium WebDriver's first result on google.
    search_result_page = (By.CLASS_NAME, 'LC20lb')
    # Download box menu from header
    download_menu = (By.ID, 'menu_download')
    # DownloadBox ---Download link for selenium---
    # in the right side menu up to donate section
    download_box = (By.CLASS_NAME, 'downloadBox')
    time = 5

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, self.time)

    def test_search_automation(self):
        # navigate to the google home page
        self.driver.get("http://www.google.com/")
        assert self.is_element_present(self.search_field)
        assert self.presence_of_element(self.feeling_lucky)
        assert self.is_element_present(self.mic_search)
        assert self.presence_of_element(self.search_box_button)
        assert self.presence_of_element(self.square_dots)
        # get the search textbox, search for keywords and submit
        self.google_search(self.search_field)
        # First result on  google search (the class name of Selenium webdriver)
        self.click_element(self.search_result_page)
        assert self.presence_of_element(self.footer_logo)
        assert self.presence_of_element(self.download_menu)
        assert self.presence_of_element(self.download_box)

    def tearDown(self):
        self.driver.quit()  # close the browser window

    def google_search(self, element):
        elem = self.get_element(element)
        elem.send_keys('Selenium WebDriver')
        elem.submit()

    def is_element_present(self, selector_value):
        try:
            element = self.wait.until(ec.visibility_of_element_located(selector_value))
            return element.is_displayed()
        except TimeoutException:
            return False

    def click_element(self, element):
        elem = self.wait.until(ec.element_to_be_clickable(element))
        elem.click()

    def check_element_is_present(self, element):
        elem = self.get_element(element)
        return elem.is_displayed()

    def get_element(self, selector_value):
        element = self.wait.until(ec.visibility_of_element_located(selector_value))
        return element

    def click_elem(self, selector_value):
        element = self.get_element(selector_value)
        element.click()

    def presence_of_element(self, selector_value):
        element = self.wait.until(ec.presence_of_element_located(selector_value))
        return element


if __name__ == '__main__':
    unittest.main()
