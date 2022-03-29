from selenium import webdriver
import time 

<<<<<<< HEAD
link = "http://suninjuly.github.io/simple_form_find_task.html"
=======
link = "http://suninjuly.github.io/find_xpath_form"
>>>>>>> eca256d (изменил селектор)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
<<<<<<< HEAD
    button = browser.find_element_by_css_selector("button.btn")
=======
    button = browser.find_element_by_css_selector("[type='submit']")
>>>>>>> eca256d (изменил селектор)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла