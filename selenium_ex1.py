import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()                               # create a new Chrome session
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")                    # navigate to the google home page


    def test_search_automation(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))   # check search box exists on Home page
        self.assertTrue(self.is_element_present(By.NAME,'btnI'))    #Name of the I'm Feeling Lucky box
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'hb2Smf'))    #Check's the class name for "search by mic"
        self.assertTrue(self.is_element_present(By.CLASS_NAME,'gNO89b'))        #Check's Google Search-box class name
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'gb_Of'))            # Check's for the google apps square dots near google account
        self.search_field = self.driver.find_element_by_name('q')    # get the search textbox
        self.search_field.send_keys('Selenium WebDriver')            # enter search keyword and submit
        self.search_field.submit()
        self.driver.find_element_by_class_name('ellip').click()      #First result on google search (the class name of Selenium webdriver)
        self.driver.find_elements_by_link_text('https://www.seleniumhq.org/projects/webdriver/')  ## Check's the link of the site
        self.assertTrue(self.is_element_present(By.ID, 'footerLogo'))
        self.assertTrue(self.is_element_present(By.ID, 'menu_download'))              #Check's the Download box menu from header
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'downloadBox'))   # Check's the DownloadBox ---Download link for selenium--- in the right side menu up to donate section


    def tearDown(self):
        self.driver.quit()                                           # close the browser window


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True


if __name__ == '__main__':
    unittest.main()