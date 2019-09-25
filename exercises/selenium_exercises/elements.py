from selenium.webdriver.common.by import By
from ja_lp.utils.baseselenium import SeleniumActions

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
    # the footer logo from selenium WebDiver site
    footer_logo = (By.ID, 'footerLogo')
    # Class name of Selenium WebDriver's first result on google.
    search_result_page = (By.CLASS_NAME, 'LC20lb')
    # Download box menu from header
    download_menu = (By.ID, 'menu_download')
    # DownloadBox ---Download link for selenium---
    # in the right side menu up to donate section
    download_box = (By.CLASS_NAME, 'downloadBox')


    def google_search(self, element):
        elem = self.get_element(element)
        elem.send_keys('Selenium WebDriver')
        elem.submit()

    def click_link(self):
        return self.click_element(self.search_result_page)

    def search_string(self):
        return self.google_search(self.search_field)

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

    def check_footer_logo(self):
        return self.presence_of_element(self.footer_logo)

    def check_download_box(self):
        return self.presence_of_element(self.download_box)

    def check_download_menu(self):
        return self.presence_of_element(self.download_menu)