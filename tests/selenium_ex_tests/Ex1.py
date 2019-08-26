from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.google.com')

q = driver.find_element(By.NAME, 'q')
q.send_keys('selenium webdriver')
driver.get('https://www.seleniumhq.org/projects/webdriver/')

driver.quit()


