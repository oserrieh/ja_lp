import unittest
from selenium import webdriver

from ja_lp.exercises.selenium_exercises.elements import GooglePageElements


class SearchText(unittest.TestCase, GooglePageElements):

    def setUp(self):
        # create a new Chrome session
        self.driver.get("http://www.google.com/")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_automation(self):
        # navigate to the google home page
        assert self.check_search_element_present()
        assert self.check_lucky_present()
        assert self.check_lucky_present()
        assert self.check_searchbox_present()
        assert self.check_square_dots()
        # get the search textbox, search for keywords and submit
        self.google_search(self.search_field)
        # First result on  google search (the class name of Selenium webdriver)
        self.click_element(self.search_result_page)
        assert self.presence_of_element(self.footer_logo)
        assert self.presence_of_element(self.download_menu)
        assert self.presence_of_element(self.download_box)

    def tearDown(self):
        self.driver.quit()  # close the browser window


if __name__ == '__main__':
    unittest.main()
