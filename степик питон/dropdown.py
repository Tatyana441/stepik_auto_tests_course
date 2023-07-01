from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html" 
browser = webdriver.Chrome() 
browser.get(link) 

number1 = browser.find_element(By.ID, "num1") # находим числа, кот нужно посчитать - number1 + number2
number2 = browser.find_element(By.ID, "num2")

x = number1.text
y = number2.text
sum = int(x) + int(y) # складываем эти числа, приводя к типу интеджер

select = Select(browser.find_element(By.TAG_NAME, "select")) # находим число в дроп дауне, подходящее сумме и выбираем как тип строка, сравниваем 
select.select_by_value(str(sum))

button = browser.find_element(By.CLASS_NAME, "btn.btn-default") # кликаем на отправить
button.click()

time.sleep(10)
browser.quit()
