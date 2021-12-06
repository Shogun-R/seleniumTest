from creds import * #your credentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

def button_press(list = []):
    total_len = sum(len(i) for i in list)
    inline_control = pyautogui
    for cycle in total_len:
        button = list[cycle]
        inline_control.press(button)


PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
debug = 10
debug0 = debug + 5
debug1 = debug0 + 5
browser = webdriver.Chrome(PATH)
wait = WebDriverWait(webdriver, 10)
control = pyautogui

print(control._pyautogui_win._size())
print(control.position())
control.moveTo(910, 145)
try:
    browser.get('https://typistapp.ca/#/home')
    browser.implicitly_wait(30)
    browser.maximize_window()
    browser.find_element_by_id('usernameInput').send_keys(login)
    browser.find_element_by_id('passwordInput').send_keys(password)
    browser.find_element_by_class_name('submit').click()
    time.sleep(15)
    control.click()
    time.sleep(5)
    control.press('SPACE')
    print(debug)
    #wait.until(EC.element_to_be_clickable(('/a[contains(text(),"Lessons"]'))).click()
    #browser.find_element_by_xpath('//a[contains(@href,"#/level/1"]').click()
    print(debug0)
    print(browser.find_elements_by_id('text-to-type'))
    print(debug1)

    for element in browser.find_elements_by_id('text-to-type'):
        print('debug0')
        print(element.text)
        text_list = [element.text]
        test_text = text_list[0]
        print('this is the len: ' + f'{sum(len(i) for i in text_list)}')
        print('this is the text_list[0]: ' + f'{text_list[0]}')
        print(f'{test_text}')
        print('debug1')


except NoSuchElementException:
    pass


