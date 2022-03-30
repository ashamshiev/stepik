from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys("")
    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option2.click()
    sumbit = browser.find_element_by_css_selector('[type="submit"]').click()

   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

