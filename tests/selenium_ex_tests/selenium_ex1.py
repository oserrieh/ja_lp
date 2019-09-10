import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchText(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # create a new Chrome session
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_search_automation(self):
        self.driver.get("http://www.google.com/")  # navigate to the google home page
        self.search_field = "q"
        self.assertTrue(self.is_element_present(By.NAME,  self.search_field)) # check search box exists on Home page
        self.feeling_lucky = 'btnI'
        self.assertTrue(self.is_element_present(By.NAME, self.feeling_lucky))   # Name of the I'm Feeling Lucky box
        self.mic_search = 'hb2Smf'
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.mic_search))  # Check's the class name for "search by mic"
        self.search_box = 'gNO89b'
        self.assertTrue(self.is_element_present(By.CLASS_NAME, self.search_box))  # Check's Google Search-box class name
        self.square_dots = 'gb_Of'
        self.assertTrue(self.is_element_present(By.CLASS_NAME,self.square_dots))  # Check's for the google apps square dots near google account
        self.driver.find_element_by_name(self.search_field).send_keys('Selenium WebDriver')   # get the search textbox
        self.driver.find_element_by_name(self.search_field).submit()
        self.driver.find_element_by_class_name('LC20lb').click()  # First result on google search (the class name of Selenium webdriver)
        self.footer_logo = 'footerLogo'
        self.assertTrue(self.is_element_present(By.ID, self.footer_logo))
        self.download_menu = 'menu_download'
        self.assertTrue(self.is_element_present(By.ID, self.download_menu))  # Check's the Download box menu from header
        self.download_box = 'downloadBox'
        self.assertTrue(self.is_element_present(By.CLASS_NAME,
                                                self.download_box))  # Check's the DownloadBox ---Download link for selenium--- in the right side menu up to donate section

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
