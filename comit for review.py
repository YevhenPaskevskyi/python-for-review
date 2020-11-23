from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Alex")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Samos")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("London")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("UK")
    button = browser.find_element_by_css_selector("#submit_button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()