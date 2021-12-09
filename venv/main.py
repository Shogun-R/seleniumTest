from creds import * #your credentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy
import array as arr
import pyautogui
import time

def button_press(list):
    total_len = len(list)
    inline_control = pyautogui
    for press in range(total_len):
        print(total_len)

    for cycle in range(total_len):
        button = list[0]
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
    print(debug0)
    print(browser.find_elements_by_id('text-to-type'))
    print(debug1)
    output_list = []

    for element in browser.find_elements_by_id('text-to-type'):
        print('debug0')
        print(element.text)
        text = element.text
        print('debug1')
        print('this is the len: ' + f'{len(text)}')
        print(output_list)
        print(text)
        testout = list(text)
        print(testout)
        print(len(text))
        #button_press(testout) #that is working

except NoSuchElementException:
    pass


# TODO: figure out why all chars are put under [0] adress in text_list
# CODEGRAVEYARD
    #button_press(text_list) just testing
    #print('this is the text_list[0]: ' + f'{text_list[0]}') just testing
    #print(f'{test_text}') just testing
    # for it in range(len(text)): medeling with text inside webelement
        # output_list.insert(it,text) trying to do proper list
        # output_list.remove(list(text))    trying to remove all unneccessary stuff
    #wait.until(EC.element_to_be_clickable(('/a[contains(text(),"Lessons"]'))).click() that thing was not able to find element
    #browser.find_element_by_xpath('//a[contains(@href,"#/level/1"]').click() that was not able to find element
    # test_array = numpy.array() not the C++ arrays :(
    # test_text = text_list[0] all the text from web element is out in one single list slot or whatever it is called