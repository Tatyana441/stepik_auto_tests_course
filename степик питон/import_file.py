from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Танечка")
input1 = browser.find_element(By.NAME, "lastname")
input1.send_keys("Иванова")
input1 = browser.find_element(By.NAME, "email")
input1.send_keys("edu@edu.ru")

with open("test.txt", "w") as file:
    content = file.write("automationbypython")

upload_button = browser.find_element(By.NAME, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt')         # добавляем к этому пути имя файла 
upload_button.send_keys(file_path)    

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

time.sleep(10)
browser.quit()