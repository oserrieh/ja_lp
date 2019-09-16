import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
    square_dots = 'gb_C'
    # the footer logo from selenium WebDiver site
    footer_logo = 'footerLogo'
    # Class name of Selenium Webdriver's first result on google.
    get_page = 'LC20lb'
    # Download box menu from header
    download_menu = 'menu_download'
    # DownloadBox ---Download link for selenium---
    # in the right side menu up to donate section
    download_box = 'downloadBox'
    time = 5

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, self.time)

    def test_search_automation(self):
        # navigate to the google home page
        self.driver.get("http://www.google.com/")
        self.wait.until(ec.visibility_of_element_located((By.NAME, self.search_field)))
        self.wait.until(ec.presence_of_element_located((By.NAME, self.feeling_lucky)))
        self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, self.mic_search)))
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, self.search_box_button)))
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, self.square_dots)))
        # get the search textbox, search for keywords and submit
        search_for = self.wait.until(ec.element_to_be_clickable((By.NAME, self.search_field)))
        search_for.send_keys('Selenium WebDriver')
        search_for.submit()
        # First result on google search (the class name of Selenium webdriver)
        self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, self.get_page))).click()
        self.wait.until(ec.presence_of_element_located((By.ID, self.footer_logo)))
        self.wait.until(ec.presence_of_element_located((By.ID, self.download_menu)))
        self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, self.download_box)))

    def tearDown(self):
        self.driver.quit()  # close the browser window


if __name__ == '__main__':
    unittest.main()
