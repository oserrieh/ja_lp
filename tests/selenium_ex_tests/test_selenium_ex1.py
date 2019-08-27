from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://www.google.com')


try:
    driver.find_element_by_id('gbw')
    driver.find_element_by_class_name('gb_f')
    driver.find_element_by_class_name('hb2Smf')
    driver.find_elements_by_partial_link_text('/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
    print('Test passed: Elements found')
except Exception as e:
    print('Exception found', format(e))


q = driver.find_element(By.NAME, 'q')
q.send_keys('selenium webdriver')
q.submit()


first_one = driver.find_elements_by_link_text('https://www.seleniumhq.org/projects/webdriver/')[:1]
for result in first_one:
    assert "selenium webriver" in result.text.lower(), "Result does not contain 'selenium webdriver'"


driver.get('https://www.seleniumhq.org/projects/webdriver/')

try:
    driver.find_elements_by_link_text('https://www.seleniumhq.org/projects/webdriver/')
    driver.find_element_by_id('footerLogo')
    driver.find_element_by_id('menu_download')
    driver.find_element_by_class_name('downloadBox')
    print('Test passed: Elements found')


except Exception as e:
    print('Exception found', format(e))


driver.quit()