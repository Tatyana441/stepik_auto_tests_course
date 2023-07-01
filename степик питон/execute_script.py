from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html" 
browser = webdriver.Chrome() 
browser.get(link) 

number = browser.find_element(By.ID, "input_value") 
x = number.text
y = calc(x)

browser.execute_script("return arguments[0].scrollIntoView(true);", number)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)
checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()
radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()
button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(10)
browser.quit()
