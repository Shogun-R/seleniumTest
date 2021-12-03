from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

browser = webdriver.Chrome(PATH)
try:
    browser.get('https://typistapp.ca/#/home')
    browser.implicitly_wait(3000)
    browser.maximize_window()
    browser.find_element_by_id('usernameInput').send_keys('Altair4132')
    browser.find_element_by_id('passwordInput').send_keys('17082002sv')
    browser.find_element_by_class_name('submit').click()

except NoSuchElementException:
    pass
