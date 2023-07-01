from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html" # открыть эту ссылку
browser = webdriver.Chrome() # в браузере Хром
browser.get(link) # Нажать

x_element = browser.find_element(By.ID, "treasure")  # Найти на ней элемент-картинку
x = x_element.get_attribute("valuex") # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
y = calc(x)
#people_checked = x_element
#y = calc(people_checked)

input = browser.find_element(By.ID, "answer") # Найти ответ по аттрибуту
input.send_keys(y) # Ввести ответ в текстовое поле
checkbox = browser.find_element(By.ID, "robotCheckbox") # Найти элемент по аттрибуту
checkbox.click() # Отметить checkbox "I'm the robot".
radiobutton = browser.find_element(By.ID, "robotsRule") # Найти элемент по аттрибуту
radiobutton.click() # Выбрать radiobutton "Robots rule!".
button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click() # Нажать на кнопку "Submit".

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
