from ja_lp.utils.baseselenium import SeleniumActions
from selenium.webdriver.common.by import By


class SeleniumPageElements(SeleniumActions):
    # Download box menu from header
    download_menu = (By.ID, 'menu_download')
    # DownloadBox ---Download link for selenium---
    # in the right side menu up to donate section
    download_box = (By.CLASS_NAME, 'downloadBox')
    # the footer logo from selenium WebDiver site
    footer_logo = (By.ID, 'footerLogo')

    def check_footer_logo(self):
        return self.presence_of_element(self.footer_logo)

    def check_download_box(self):
        return self.presence_of_element(self.download_box)

    def check_download_menu(self):
        return self.presence_of_element(self.download_menu)
