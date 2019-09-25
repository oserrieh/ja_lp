import unittest
from selenium import webdriver

from ja_lp.exercises.selenium_exercises.elements import GooglePageElements


class SearchText(unittest.TestCase, GooglePageElements):

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com/")
        self.driver.maximize_window()

    def test_search_automation(self):
        # navigate to the google home page
        page = GooglePageElements(self.driver)
        assert page.check_search_element_present()
        assert page.check_lucky_present()
        assert page.check_mic_search()
        assert page.check_searchbox_present()
        assert page.check_square_dots()
        # get the search textbox, search for keywords and submit
        page.search_string()
        # First result on  google search (the class name of Selenium webdriver)
        page.click_link()
        assert page.check_footer_logo()
        assert page.check_download_menu()
        assert page.check_download_box()

    def tearDown(self):
        self.driver.quit()  # close the browser window


if __name__ == '__main__':
    unittest.main()
