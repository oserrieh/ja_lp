import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchText(unittest.TestCase):
    # search box from Google home page
    search_field = "q"
    # Name of the I'm Feeling Lucky box
    feeling_lucky = 'btnI'
    # the class name for "search by mic"
    mic_search = 'hb2Smf'
    # "Google Search" button class name
    search_box_button = 'gNO89b'
    # Google apps square dots near google account
    square_dots = 'gb_Of'
    # the footer logo from selenium webdriver site
    footer_logo = 'footerLogo'
    # Download box menu from header
    download_menu = 'menu_download'
    # DownloadBox ---Download link for selenium---
    # in the right side menu up to donate section
    download_box = 'downloadBox'

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_search_automation(self):
        # navigate to the google home page
        self.driver.get("http://www.google.com/")
        self.assertTrue(self.is_element_present(By.NAME, self.search_field))
        self.assertTrue(self.is_element_present(By.NAME, self.feeling_lucky))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.mic_search))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.search_box_button))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.square_dots))
        # get the search textbox, search for keywords and submit
        self.driver.find_element_by_name(self.search_field).send_keys('Selenium WebDriver')
        self.driver.find_element_by_name(self.search_field).submit()
        # First result on google search (the class name of Selenium webdriver)
        self.driver.find_element_by_class_name('LC20lb').click()
        self.assertTrue(self.is_element_present(By.ID, self.footer_logo))
        self.assertTrue(self.is_element_present(By.ID, self.download_menu))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.download_box))

    def tearDown(self):
        self.driver.quit()  # close the browser window

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True


if __name__ == '__main__':
    unittest.main()
