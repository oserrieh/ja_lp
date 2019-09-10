import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchText(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # create a new Chrome session
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_search_automation(self):
        # navigate to the google home page
        self.driver.get("http://www.google.com/")
        # check search box exists on Home page
        self.search_field = "q"
        self.assertTrue(self.is_element_present(By.NAME, self.search_field))
        # Name of the I'm Feeling Lucky box
        self.feeling_lucky = 'btnI'
        self.assertTrue(self.is_element_present(By.NAME, self.feeling_lucky))
        # Check's the class name for "search by mic"
        self.mic_search = 'hb2Smf'
        self.assertTrue(
            self.is_element_present(By.CLASS_NAME, self.mic_search))
        # Check's Google Search-box class name
        self.search_box = 'gNO89b'
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.search_box))
        # Check's for the google apps square dots near google account
        self.square_dots = 'gb_Of'
        self.assertTrue(self.is_element_present(By.CLASS_NAME,
                                                self.square_dots))

        # get the search textbox search for keywords and submit
        self.driver.find_element_by_name(self.search_field).send_keys('Selenium WebDriver')
        self.driver.find_element_by_name(self.search_field).submit()
        # First result on google search (the class name of Selenium webdriver)
        self.driver.find_element_by_class_name( 'LC20lb').click()
        # Check's the footer logo
        self.footer_logo = 'footerLogo'
        self.assertTrue(self.is_element_present(By.ID, self.footer_logo))
        # Check's the Download box menu from header
        self.download_menu = 'menu_download'
        self.assertTrue(self.is_element_present(By.ID, self.download_menu))
        # Check's the DownloadBox ---Download link for selenium---
        # in the right side menu up to donate section
        self.download_box = 'downloadBox'
        self.assertTrue(self.is_element_present(By.CLASS_NAME,
                                                self.download_box))

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
