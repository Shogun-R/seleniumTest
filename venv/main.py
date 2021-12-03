from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
debug = 10
debug0 = debug + 5
debug1 = debug0 + 5


browser = webdriver.Chrome(PATH)
try:
    browser.get('https://typistapp.ca/#/home')
    browser.implicitly_wait(30)
    browser.maximize_window()
    browser.find_element_by_id('usernameInput').send_keys('login')
    browser.find_element_by_id('passwordInput').send_keys('password')
    browser.find_element_by_class_name('submit').click()
    time.sleep(15)
    print(debug)
    WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(By.XPATH))
    print(debug)
    browser.find_element_by_xpath('//a[contains(@href,"#/level/1"]').click()
    print(debug)


except NoSuchElementException:
    pass
