from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('http://www.google.com')
driver.maximize_window()
time.sleep(2)

try:
    driver.find_element_by_class_name('gNO89b')   ##Google Search-box class name
    driver.find_element_by_name('btnI')           ##Name of the I'm Feeling Lucky box
    driver.find_elements_by_partial_link_text('/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')  ##link to google picture logo from google homepage
    print('Test passed: Elements found')
except Exception as e:
    print('Exception found', format(e))


q = driver.find_element(By.NAME, 'q')       ## Find the searchbar from google.com
q.send_keys('selenium webdriver')       ##Enter keys from keyboard
time.sleep(1)
q.submit()          ## Submit the google search

first_one = driver.find_elements_by_link_text('https://www.seleniumhq.org/projects/webdriver/')[:1]     #Check's the first google search result
for result in first_one:
    assert "selenium webriver" in result.text.lower(), "Result does not contain 'selenium webdriver'"

driver.find_element_by_class_name('ellip').click()    ## Finding the class name for the first result in google searches(Selenium WebDriver) and click's it
time.sleep(3)


try:
    driver.find_elements_by_link_text('https://www.seleniumhq.org/projects/webdriver/')     ## Check's the link of the site
    driver.find_element_by_id('footerLogo')         ## Check's the OpenGl Footer logo
    driver.find_element_by_id('menu_download')      ##Check's the Download box menu from header
    driver.find_element_by_class_name('downloadBox')        ## Check's the DownloadBox ---Download link for selenium--- in the right side menu up to donate section
    print('Test passed: Elements found')


except Exception as e:
    print('Exception found', format(e))

time.sleep(1.5)
driver.quit()
