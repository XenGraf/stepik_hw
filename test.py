from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
 
link = "http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    option1 = browser.find_element_by_css_selector('[for="robotsRule"]')
    option1.click()
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла



